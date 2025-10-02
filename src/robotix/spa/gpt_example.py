# =======================================================
# Sense–Plan–Act (SPA) skeleton with explicit Protocols
# Python 3.13 — ROS Noetic friendly (wire actions later)
# =======================================================
from dataclasses import dataclass, field
from typing import Protocol, runtime_checkable, Sequence, List, Dict, Any, Optional


# ----------------- PROTOCOLS -----------------

@runtime_checkable
class GoalProto(Protocol):
    """Abstract mission objective."""

    @property
    def name(self) -> str: ...

    def parameters(self) -> Dict[str, Any]: ...


@runtime_checkable
class ActionProto(Protocol):
    """Atomic executable step (may call ROS actions/services)."""

    @property
    def id(self) -> str: ...

    def check_preconditions(self, state: "WorldState") -> bool: ...

    def expected_cost(self, state: "WorldState") -> float: ...

    def expected_risk(self, state: "WorldState") -> float: ...

    def execute(self, state: "WorldState") -> "WorldState": ...

    def can_recover(self, error: Exception) -> bool: ...

    def recover(self, state: "WorldState", error: Exception) -> "WorldState": ...


@runtime_checkable
class PlanProto(Protocol):
    """Container of actions with evaluation hooks."""

    @property
    def id(self) -> str: ...

    @property
    def actions(self) -> Sequence[ActionProto]: ...

    def is_feasible(self, state: "WorldState") -> bool: ...

    def simulate_cost(self, state: "WorldState") -> float: ...

    def simulate_risk(self, state: "WorldState") -> float: ...


@runtime_checkable
class PlannerProto(Protocol):
    """Produces candidate plans and selects one."""

    def propose(self, goal: GoalProto, state: "WorldState") -> List[PlanProto]: ...

    def score(self, plan: PlanProto, state: "WorldState") -> float: ...

    def select(self, candidates: List[PlanProto], state: "WorldState") -> Optional[PlanProto]: ...


# ----------------- DOMAIN MODELS -----------------

@dataclass
class WorldState:
    """Fused state from Sense step (fill from ROS topics)."""
    pose: Any
    obstacles: Any
    battery: float
    risk_level: float
    extras: Dict[str, Any] = field(default_factory=dict)


# ----------------- GOALS (explicit inheritance) -----------------

@dataclass(frozen=True)
class DeliverGoal(GoalProto):
    """Deliver a payload to a dock."""
    dock_id: str
    payload_id: str = "default"

    @property
    def name(self) -> str:
        return "deliver"

    def parameters(self) -> Dict[str, Any]:
        return {"dock_id": self.dock_id, "payload_id": self.payload_id}


# ----------------- ACTIONS (explicit inheritance) -----------------

@dataclass
class GoToWaypoint(ActionProto):
    """Navigate to a named waypoint."""
    wp: str

    @property
    def id(self) -> str:
        return f"goto:{self.wp}"

    def check_preconditions(self, state: WorldState) -> bool:
        # Example: map available, localization healthy, not in failsafe
        return True

    def expected_cost(self, state: WorldState) -> float:
        # Replace with distance/time/energy estimate
        return 5.0

    def expected_risk(self, state: WorldState) -> float:
        # Replace with collision/uncertainty estimate
        return 0.2

    def execute(self, state: WorldState) -> WorldState:
        # TODO: send ROS action/service/command; wait/result handling
        return state

    def can_recover(self, error: Exception) -> bool:
        return True

    def recover(self, state: WorldState, error: Exception) -> WorldState:
        # TODO: local replan, costmap inflate, retry, etc.
        return state


@dataclass
class CorridorFollow(ActionProto):
    """Follow a corridor sector (example higher-level motion primitive)."""
    sector_id: str

    @property
    def id(self) -> str:
        return f"corridor:{self.sector_id}"

    def check_preconditions(self, state: WorldState) -> bool:
        return True

    def expected_cost(self, state: WorldState) -> float:
        return 7.0

    def expected_risk(self, state: WorldState) -> float:
        return 0.1

    def execute(self, state: WorldState) -> WorldState:
        return state

    def can_recover(self, error: Exception) -> bool:
        return True

    def recover(self, state: WorldState, error: Exception) -> WorldState:
        return state


@dataclass
class DockAt(ActionProto):
    """Dock/land/attach at a station."""
    dock_id: str

    @property
    def id(self) -> str:
        return f"dock:{self.dock_id}"

    def check_preconditions(self, state: WorldState) -> bool:
        # Example: pose near dock, docking station available
        return True

    def expected_cost(self, state: WorldState) -> float:
        return 3.0

    def expected_risk(self, state: WorldState) -> float:
        return 0.05

    def execute(self, state: WorldState) -> WorldState:
        return state

    def can_recover(self, error: Exception) -> bool:
        return False

    def recover(self, state: WorldState, error: Exception) -> WorldState:
        return state


# ----------------- PLAN (explicit inheritance) -----------------

@dataclass
class SequentialPlan(PlanProto):
    """A simple sequence of actions executed in order."""
    plan_id: str
    _actions: List[ActionProto]

    @property
    def id(self) -> str:
        return self.plan_id

    @property
    def actions(self) -> Sequence[ActionProto]:
        return self._actions

    def is_feasible(self, state: WorldState) -> bool:
        return all(a.check_preconditions(state) for a in self._actions)

    def simulate_cost(self, state: WorldState) -> float:
        return sum(a.expected_cost(state) for a in self._actions)

    def simulate_risk(self, state: WorldState) -> float:
        return max((a.expected_risk(state) for a in self._actions), default=0.0)


# ----------------- PLANNER (explicit inheritance) -----------------

class EnergyRiskPlanner(PlannerProto):
    """Offer distinct plans (short&busy vs long&safe) and score them."""

    def propose(self, goal: GoalProto, state: WorldState) -> List[PlanProto]:
        params = goal.parameters()
        dock = params["dock_id"]

        p_short = SequentialPlan(
            plan_id="short_busy",
            _actions=[
                GoToWaypoint("wp_fast1"),
                GoToWaypoint("wp_fast2"),
                DockAt(dock),
            ],
        )

        p_safe = SequentialPlan(
            plan_id="long_safe",
            _actions=[
                GoToWaypoint("wp_safe1"),
                CorridorFollow("sector_A"),
                GoToWaypoint("wp_safe2"),
                DockAt(dock),
            ],
        )

        return [p for p in (p_short, p_safe) if p.is_feasible(state)]

    def score(self, plan: PlanProto, state: WorldState) -> float:
        # Lower is better: tune weights to your mission policy
        c = plan.simulate_cost(state)
        r = plan.simulate_risk(state)
        battery_penalty = 10.0 if (state.battery < 0.20 and plan.id == "short_busy") else 0.0
        return 0.7 * c + 0.3 * r + battery_penalty

    def select(self, candidates: List[PlanProto], state: WorldState) -> Optional[PlanProto]:
        return min(candidates, key=lambda p: self.score(p, state), default=None)


# ----------------- SPA ORCHESTRATOR -----------------

class SPAController:
    """Sense → Plan → Act loop with plan retention and re-evaluation."""

    def __init__(self, planner: PlannerProto):
        self.planner = planner
        self.current_plan: Optional[PlanProto] = None

    # --- SENSE ---
    def sense(self) -> WorldState:
        # TODO: fuse ROS topics (odom, lidar, battery, etc.)
        return WorldState(pose=None, obstacles=None, battery=0.55, risk_level=0.1)

    # --- PLAN ---
    def plan(self, goal: GoalProto, state: WorldState) -> Optional[PlanProto]:
        candidates = self.planner.propose(goal, state)
        return self.planner.select(candidates, state)

    # --- ACT ---
    def act(self, plan: PlanProto, state: WorldState) -> WorldState:
        for a in plan.actions:
            try:
                state = a.execute(state)
            except Exception as e:
                if a.can_recover(e):
                    state = a.recover(state, e)
                else:
                    raise
        return state

    # --- ONE CYCLE ---
    def tick(self, goal: GoalProto) -> WorldState:
        state = self.sense()
        # (Re)plan if none or not feasible anymore
        if self.current_plan is None or not self.current_plan.is_feasible(state):
            self.current_plan = self.plan(goal, state)
            if self.current_plan is None:
                raise RuntimeError("No feasible plan for the given goal.")
        return self.act(self.current_plan, state)


# ----------------- EXAMPLE MAIN -----------------

if __name__ == "__main__":
    controller = SPAController(EnergyRiskPlanner())
    goal = DeliverGoal(dock_id="D1")
    # Optional runtime check (shallow) — thanks to @runtime_checkable
    assert isinstance(goal, GoalProto)
    final_state = controller.tick(goal)
