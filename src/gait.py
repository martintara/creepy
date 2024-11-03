# gait.py
import time
class Gait:
    def __init__(self, creepy_pod):
        """
        Initialize the Gait with a reference to the CreepyPod instance.
        This allows the gait to control individual leg movements.
        """
        self.creepy_pod = creepy_pod

    def tripod_gait(self):
        # Phase 1: Move legs 0, 3, and 4
        self.creepy_pod.legs[0].leg_forward()
        self.creepy_pod.legs[1].leg_forward()
        self.creepy_pod.legs[2].leg_forward()
        self.creepy_pod.legs[3].leg_forward()
        self.creepy_pod.legs[4].leg_forward()
        self.creepy_pod.legs[5].leg_forward()
#       time.sleep(2)
#       self.creepy_pod.legs[0].leg_backward()
#       self.creepy_pod.legs[1].leg_backward()
#       self.creepy_pod.legs[2].leg_backward()
#       self.creepy_pod.legs[3].leg_backward()
#       self.creepy_pod.legs[4].leg_backward()
#       self.creepy_pod.legs[5].leg_backward()

    def wave_gait(self):
        """
        ?
        """
