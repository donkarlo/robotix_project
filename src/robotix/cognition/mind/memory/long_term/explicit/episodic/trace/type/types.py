from enum import Enum, auto

class Types(Enum):
    mission = auto()
    pre_plan = auto()
    plan = auto()
    action = auto()
    command = auto()
    sensor_ob = auto()
    ditributed_kinematic = auto()
    lidar_scan_ranges = auto()
