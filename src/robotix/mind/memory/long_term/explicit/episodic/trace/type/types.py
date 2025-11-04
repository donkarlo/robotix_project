from enum import Enum, auto

class Types(Enum):
    mission = auto()
    pre_plan = auto()
    plan = auto()
    action = auto()
    command = auto()
    sensor_ob = auto()
    ditributed_quaternion_kinematic = auto()
    lidar_scan_ranges = auto()
    human_command_remeber_experience = auto()
