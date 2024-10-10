from enum import Enum

class CreepyState(Enum):
    """
    Different states of CreepyPod
    """
    STARTUP = 0
    IDLE = 1
    MANUAL = 2
    AUTO = 3
    SHUTDOWN = 4
