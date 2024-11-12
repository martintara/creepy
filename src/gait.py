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
        self.creepy_pod.legs[0].leg_forward()
        self.creepy_pod.legs[2].leg_forward()
        self.creepy_pod.legs[4].leg_forward()
        self.creepy_pod.legs[1].leg_backward()
        self.creepy_pod.legs[3].leg_backward()
        self.creepy_pod.legs[5].leg_backward()
        time.sleep(1)
        self.creepy_pod.legs[0].lower_leg()
        self.creepy_pod.legs[2].lower_leg()
        self.creepy_pod.legs[4].lower_leg()
        self.creepy_pod.legs[1].rise_leg()
        self.creepy_pod.legs[3].rise_leg()
        self.creepy_pod.legs[5].rise_leg()
        time.sleep(1)
        self.creepy_pod.legs[0].leg_backward()
        self.creepy_pod.legs[2].leg_backward()
        self.creepy_pod.legs[4].leg_backward()
        self.creepy_pod.legs[1].leg_forward()
        self.creepy_pod.legs[3].leg_forward()
        self.creepy_pod.legs[5].leg_forward()
        time.sleep(1)
        self.creepy_pod.legs[0].rise_leg()
        self.creepy_pod.legs[2].rise_leg()
        self.creepy_pod.legs[4].rise_leg()
        self.creepy_pod.legs[1].lower_leg()
        self.creepy_pod.legs[3].lower_leg()
        self.creepy_pod.legs[5].lower_leg()
        time.sleep(1)

    def rotate_tripod_right(self):
        self.creepy_pod.legs[0].lower_leg()
        self.creepy_pod.legs[2].lower_leg()
        self.creepy_pod.legs[4].lower_leg()
        self.creepy_pod.legs[1].rise_leg()
        self.creepy_pod.legs[3].rise_leg()
        self.creepy_pod.legs[5].rise_leg()
        time.sleep(1)
        self.creepy_pod.legs[1].leg_forward()
        self.creepy_pod.legs[3].leg_backward()
        self.creepy_pod.legs[5].leg_backward()
        self.creepy_pod.legs[0].leg_backward()
        self.creepy_pod.legs[2].leg_backward()
        self.creepy_pod.legs[4].leg_forward()
        time.sleep(1)
        self.creepy_pod.legs[0].rise_leg()
        self.creepy_pod.legs[2].rise_leg()
        self.creepy_pod.legs[4].rise_leg()
        self.creepy_pod.legs[1].lower_leg()
        self.creepy_pod.legs[3].lower_leg()
        self.creepy_pod.legs[5].lower_leg()
        time.sleep(1)
        self.creepy_pod.legs[1].leg_backward()
        self.creepy_pod.legs[3].leg_forward()
        self.creepy_pod.legs[5].leg_forward()
        self.creepy_pod.legs[0].leg_forward()
        self.creepy_pod.legs[2].leg_forward()
        self.creepy_pod.legs[4].leg_backward()
        time.sleep(1)

    def rotate_tripod_left(self):
        self.creepy_pod.legs[0].lower_leg()
        self.creepy_pod.legs[2].lower_leg()
        self.creepy_pod.legs[4].lower_leg()
        self.creepy_pod.legs[1].rise_leg()
        self.creepy_pod.legs[3].rise_leg()
        self.creepy_pod.legs[5].rise_leg()
        time.sleep(1)
        self.creepy_pod.legs[1].leg_backward()
        self.creepy_pod.legs[3].leg_forward()
        self.creepy_pod.legs[5].leg_forward()
        self.creepy_pod.legs[0].leg_forward()
        self.creepy_pod.legs[2].leg_forward()
        self.creepy_pod.legs[4].leg_backward()
        time.sleep(1)
        self.creepy_pod.legs[0].rise_leg()
        self.creepy_pod.legs[2].rise_leg()
        self.creepy_pod.legs[4].rise_leg()
        self.creepy_pod.legs[1].lower_leg()
        self.creepy_pod.legs[3].lower_leg()
        self.creepy_pod.legs[5].lower_leg()
        time.sleep(1)
        self.creepy_pod.legs[1].leg_forward()
        self.creepy_pod.legs[3].leg_backward()
        self.creepy_pod.legs[5].leg_backward()
        self.creepy_pod.legs[0].leg_backward()
        self.creepy_pod.legs[2].leg_backward()
        self.creepy_pod.legs[4].leg_forward()
        time.sleep(1)


    def wave_gait(self):
        """
        ?
        """
