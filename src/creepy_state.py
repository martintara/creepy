from enum import Enum

class CreepyState(Enum):
    """
    Different states of CreepyPod
    """
    DEVMODE = 0
    STARTUP = 1
    IDLE = 2
    MANUAL = 3
    AUTO = 4
    SHUTDOWN = 5
    EXIT = 6
    DEVMODE2 = 7
    DEVMODE3 = 8
