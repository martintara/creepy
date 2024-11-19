# gait.py
import time
import threading

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

    def rotate_tripod_left(self):
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

    def rotate_tripod_right(self):
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

    def ik_gait(self):
        # self.legs[0].move_to_global_position(175, 100, -150)
        # time.sleep(2)
        self.legs[0].draw_straight_line(175, 100, -150, 175, 200, -150, steps=20)
        time.sleep(2)
        self.legs[0].draw_straight_line(175, 200, -150, 175, 200, -100, steps=20)
        time.sleep(2)
        self.legs[0].draw_straight_line(175, 200, -100, 175, 100, -100, steps=20)
        time.sleep(2)
        self.legs[0].draw_straight_line(175, 100, -100, 175, 100, -150, steps=20)
        time.sleep(2)

        self.legs[2].draw_straight_line(175, 100, -150, 175, 200, -150, steps=20)
        time.sleep(2)
        self.legs[2].draw_straight_line(175, 200, -150, 175, 200, -100, steps=20)
        time.sleep(2)
        self.legs[2].draw_straight_line(175, 200, -100, 175, 100, -100, steps=20)
        time.sleep(2)
        self.legs[2].draw_straight_line(175, 100, -100, 175, 100, -150, steps=20)
        time.sleep(2)

def draw_straight_line_two_legs(self):
    """
    Draw straight lines for two legs simultaneously using the `draw_straight_line` method of the `Leg` class.
    
    Parameters:
    - leg1, leg2: Instances of the `Leg` class.
    - start1, end1: Start and end positions for leg1 (tuples of x, y, z).
    - start2, end2: Start and end positions for leg2 (tuples of x, y, z).
    - steps: Number of steps for the line drawing.
    """
    def move_leg1():
        self.legs[0].draw_straight_line(175, 100, -150, 175, 200, -150, steps=20)
        time.sleep(2)
        self.legs[0].draw_straight_line(175, 200, -150, 175, 200, -100, steps=20)
        time.sleep(2)
        self.legs[0].draw_straight_line(175, 200, -100, 175, 100, -100, steps=20)
        time.sleep(2)
        self.legs[0].draw_straight_line(175, 100, -100, 175, 100, -150, steps=20)
        time.sleep(2)

    def move_leg2():
        self.legs[2].draw_straight_line(175, -300, -150, 175, -200, -150, steps=20)
        time.sleep(2)
        self.legs[2].draw_straight_line(175, -200, -150, 175, -200, -100, steps=20)
        time.sleep(2)
        self.legs[2].draw_straight_line(175, -200, -100, 175, -300, -100, steps=20)
        time.sleep(2)
        self.legs[2].draw_straight_line(175, -300, -100, 175, -300, -150, steps=20)
        time.sleep(2)



    # Create threads for each leg
    thread1 = threading.Thread(target=move_leg1)
    thread2 = threading.Thread(target=move_leg2)

    # Start the threads
    thread1.start()
    thread2.start()

    # Wait for both threads to complete
    thread1.join()
    thread2.join()



    def wave_gait(self):
        """
        ?
        """
