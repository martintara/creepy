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
        self.creepy_pod.legs[0].draw_straight_line(175, 100, -150, 175, 200, -150, steps=20)
        time.sleep(2)
        self.creepy_pod.legs[0].draw_straight_line(175, 200, -150, 175, 200, -100, steps=20)
        time.sleep(2)
        self.creepy_pod.legs[0].draw_straight_line(175, 200, -100, 175, 100, -100, steps=20)
        time.sleep(2)
        self.creepy_pod.legs[0].draw_straight_line(175, 100, -100, 175, 100, -150, steps=20)
        time.sleep(2)

        self.creepy_pod.legs[2].draw_straight_line(175, 100, -150, 175, 200, -150, steps=20)
        time.sleep(2)
        self.creepy_pod.legs[2].draw_straight_line(175, 200, -150, 175, 200, -100, steps=20)
        time.sleep(2)
        self.creepy_pod.legs[2].draw_straight_line(175, 200, -100, 175, 100, -100, steps=20)
        time.sleep(2)
        self.creepy_pod.legs[2].draw_straight_line(175, 100, -100, 175, 100, -150, steps=20)
        time.sleep(2)

    def draw_straight_line_two_legs(self):
#        def move_leg0():
#            self.creepy_pod.legs[0].draw_straight_line(inital_0x, initial_0y, initial_0z, initial_0x, initial_0y + 100, initial_0z, steps=20)
#            time.sleep(2)
#            self.creepy_pod.legs[0].draw_straight_line(inital_0x, initial_0y + 100, initial_0z, initial_0x, initial_0y + 100, initial_0z+50, steps=20)
#            time.sleep(2)
#            self.creepy_pod.legs[0].draw_straight_line(inital_0x, initial_0y + 100, initial_0z+50, initial_0x, initial_0y, initial_0z+50, steps=20)
#            time.sleep(2)
#            self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y, initial_0z+50, initial_0x, initial_0y, initial_0z, steps=20)
#            time.sleep(2)

        def move_leg0():
            self.creepy_pod.legs[0].draw_straight_line(175, 200, -150, 175, 300, -150, steps=20)
            time.sleep(2)
            self.creepy_pod.legs[0].draw_straight_line(175, 300, -150, 175, 300, -100, steps=20)
            time.sleep(2)
            self.creepy_pod.legs[0].draw_straight_line(175, 300, -100, 175, 200, -100, steps=20)
            time.sleep(2)
            self.creepy_pod.legs[0].draw_straight_line(175, 200, -100, 175, 200, -150, steps=20)
            time.sleep(2)



        def move_leg2():
            self.creepy_pod.legs[2].draw_straight_line(175, -300, -150, 175, -200, -150, steps=20)
            time.sleep(2)
            self.creepy_pod.legs[2].draw_straight_line(175, -200, -150, 175, -200, -100, steps=20)
            time.sleep(2)
            self.creepy_pod.legs[2].draw_straight_line(175, -200, -100, 175, -300, -100, steps=20)
            time.sleep(2)
            self.creepy_pod.legs[2].draw_straight_line(175, -300, -100, 175, -300, -150, steps=20)
            time.sleep(2)

        def move_leg4():
            self.creepy_pod.legs[4].draw_straight_line(-425, -50, -150, -425, 50, -150, steps=20)
            time.sleep(2)
            self.creepy_pod.legs[4].draw_straight_line(-425, 50, -150, -425, 50, -100, steps=20)
            time.sleep(2)
            self.creepy_pod.legs[4].draw_straight_line(-425, 50, -100, -425, -50, -100, steps=20)
            time.sleep(2)
            self.creepy_pod.legs[4].draw_straight_line(-425, -50, -100, -425, -50, -150, steps=20)
            time.sleep(2)



        # Create threads for each leg
        thread0 = threading.Thread(target=move_leg0)
        thread2 = threading.Thread(target=move_leg2)
        thread4 = threading.Thread(target=move_leg4)

        # Start the threads
        thread0.start()
        thread2.start()
        thread4.start()

        # Wait for both threads to complete
        thread0.join()
        thread2.join()
        thread4.join()



    def wave_gait(self):
        """
        ?
        """
