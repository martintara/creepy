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

    # A simplified gait based on preprogrammed positions
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
        self.creepy_pod.legs[0].draw_straight_line(175, 100, -150, 175, 200, -150, delay, steps=20)
        time.sleep(2)
        self.creepy_pod.legs[0].draw_straight_line(175, 200, -150, 175, 200, -100, delay, steps=20)
        time.sleep(2)
        self.creepy_pod.legs[0].draw_straight_line(175, 200, -100, 175, 100, -100, delay, steps=20)
        time.sleep(2)
        self.creepy_pod.legs[0].draw_straight_line(175, 100, -100, 175, 100, -150, delay, steps=20)
        time.sleep(2)

        self.creepy_pod.legs[2].draw_straight_line(175, 100, -150, 175, 200, -150, delay, steps=20)
        time.sleep(2)
        self.creepy_pod.legs[2].draw_straight_line(175, 200, -150, 175, 200, -100, delay, steps=20)
        time.sleep(2)
        self.creepy_pod.legs[2].draw_straight_line(175, 200, -100, 175, 100, -100, delay, steps=20)
        time.sleep(2)
        self.creepy_pod.legs[2].draw_straight_line(175, 100, -100, 175, 100, -150, delay, steps=20)
        time.sleep(2)


    # Leg movement based on inverse kinematics and a global coordinate system
    def ripple_gait(self, 
                                    initial_0x, initial_0y, initial_0z,
                                    initial_1x, initial_1y, initial_1z,
                                    initial_2x, initial_2y, initial_2z, 
                                    initial_3x, initial_3y, initial_3z, 
                                    initial_4x, initial_4y, initial_4z, 
                                    initial_5x, initial_5y, initial_5z, length, height, delay):
        def move_leg0():
            time.sleep(3*delay*20)
            self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y + length, initial_0z, initial_0x, initial_0y, initial_0z, delay, steps=20) # back
            time.sleep(2*delay*20)
            self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y, initial_0z, initial_0x, initial_0y, initial_0z + height, delay, steps=20) # up
            self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y, initial_0z + height, initial_0x, initial_0y + length, initial_0z + height, delay, steps=20) # forward
            self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y + length, initial_0z + height, initial_0x, initial_0y + length, initial_0z, delay, steps=20) # down
            self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y + length, initial_0z, initial_0x, initial_0y, initial_0z, delay, steps=20) # back
            time.sleep(2*delay*20)
            time.sleep(3*delay*20)
            self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y, initial_0z, initial_0x, initial_0y, initial_0z + height, delay, steps=20) # up
            self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y, initial_0z + height, initial_0x, initial_0y + length, initial_0z + height, delay, steps=20) # forward
            self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y + length, initial_0z + height, initial_0x, initial_0y + length, initial_0z, delay, steps=20) # down


        def move_leg1():
            self.creepy_pod.legs[1].draw_straight_line(initial_1x, initial_1y, initial_1z, initial_1x, initial_1y, initial_1z + height, delay, steps=20) #up
            self.creepy_pod.legs[1].draw_straight_line(initial_1x, initial_1y, initial_1z + height, initial_1x, initial_1y + length, initial_1z + height, delay, steps=20) # forward
            self.creepy_pod.legs[1].draw_straight_line(initial_1x, initial_1y + length, initial_1z + height, initial_1x, initial_1y + length, initial_1z, delay, steps=20) # down
            self.creepy_pod.legs[1].draw_straight_line(initial_1x, initial_1y + length, initial_1z, initial_1x, initial_1y, initial_1z, delay, steps=20) # back
            time.sleep(2*delay*20)
            time.sleep(3*delay*20)
            self.creepy_pod.legs[1].draw_straight_line(initial_1x, initial_1y, initial_1z, initial_1x, initial_1y, initial_1z + height, delay, steps=20) #up
            self.creepy_pod.legs[1].draw_straight_line(initial_1x, initial_1y, initial_1z + height, initial_1x, initial_1y + length, initial_1z + height, delay, steps=20) # forward
            self.creepy_pod.legs[1].draw_straight_line(initial_1x, initial_1y + length, initial_1z + height, initial_1x, initial_1y + length, initial_1z, delay, steps=20) # down
            time.sleep(3*delay*20)
            self.creepy_pod.legs[1].draw_straight_line(initial_1x, initial_1y + length, initial_1z, initial_1x, initial_1y, initial_1z, delay, steps=20) # back

        def move_leg2():
            time.sleep(3*delay*20)
            self.creepy_pod.legs[2].draw_straight_line(initial_2x, initial_2y, initial_2z, initial_2x, initial_2y, initial_2z + height, delay, steps=20) # up
            self.creepy_pod.legs[2].draw_straight_line(initial_2x, initial_2y, initial_2z + height, initial_2x, initial_2y + length, initial_2z + height, delay, steps=20) # forward
            self.creepy_pod.legs[2].draw_straight_line(initial_2x, initial_2y + length, initial_2z + height, initial_2x, initial_2y + length, initial_2z, delay, steps=20) # down
            time.sleep(3*delay*20)
            self.creepy_pod.legs[2].draw_straight_line(initial_2x, initial_2y + length, initial_2z, initial_2x, initial_2y, initial_2z, delay, steps=20) # back
            time.sleep(2*delay*20)
            self.creepy_pod.legs[2].draw_straight_line(initial_2x, initial_2y, initial_2z, initial_2x, initial_2y, initial_2z + height, delay, steps=20) # up
            self.creepy_pod.legs[2].draw_straight_line(initial_2x, initial_2y, initial_2z + height, initial_2x, initial_2y + length, initial_2z + height, delay, steps=20) # forward
            self.creepy_pod.legs[2].draw_straight_line(initial_2x, initial_2y + length, initial_2z + height, initial_2x, initial_2y + length, initial_2z, delay, steps=20) # down
            self.creepy_pod.legs[2].draw_straight_line(initial_2x, initial_2y + length, initial_2z, initial_2x, initial_2y, initial_2z, delay, steps=20) # back

        def move_leg3():
            time.sleep(3*delay*20)
            self.creepy_pod.legs[3].draw_straight_line(initial_3x, initial_3y + length, initial_3z, initial_3x, initial_3y, initial_3z, delay, steps=20) # back
            time.sleep(2*delay*20)
            self.creepy_pod.legs[3].draw_straight_line(initial_3x, initial_3y, initial_3z, initial_3x, initial_3y, initial_3z + height, delay, steps=20) #up
            self.creepy_pod.legs[3].draw_straight_line(initial_3x, initial_3y, initial_3z + height, initial_3x, initial_3y + length, initial_3z + height, delay, steps=20) # forward
            self.creepy_pod.legs[3].draw_straight_line(initial_3x, initial_3y + length, initial_3z + height, initial_3x, initial_3y + length, initial_3z, delay, steps=20) # down
            self.creepy_pod.legs[3].draw_straight_line(initial_3x, initial_3y + length, initial_3z, initial_3x, initial_3y, initial_3z, delay, steps=20) # back
            time.sleep(2*delay*20)
            time.sleep(3*delay*20)
            self.creepy_pod.legs[3].draw_straight_line(initial_3x, initial_3y, initial_3z, initial_3x, initial_3y, initial_3z + height, delay, steps=20) #up
            self.creepy_pod.legs[3].draw_straight_line(initial_3x, initial_3y, initial_3z + height, initial_3x, initial_3y + length, initial_3z + height, delay, steps=20) # forward
            self.creepy_pod.legs[3].draw_straight_line(initial_3x, initial_3y + length, initial_3z + height, initial_3x, initial_3y + length, initial_3z, delay, steps=20) # down


        def move_leg4():
            self.creepy_pod.legs[4].draw_straight_line(initial_4x, initial_4y, initial_4z, initial_4x, initial_4y, initial_4z + height, delay, steps=20) #up
            self.creepy_pod.legs[4].draw_straight_line(initial_4x, initial_4y, initial_4z + height, initial_4x, initial_4y + length, initial_4z + height, delay, steps=20) #forward
            self.creepy_pod.legs[4].draw_straight_line(initial_4x, initial_4y + length, initial_4z + height, initial_4x, initial_4y + length, initial_4z, delay, steps=20) #down
            self.creepy_pod.legs[4].draw_straight_line(initial_4x, initial_4y + length, initial_4z, initial_4x, initial_4y, initial_4z, delay, steps=20) #back
            time.sleep(2*delay*20)
            time.sleep(3*delay*20)
            self.creepy_pod.legs[4].draw_straight_line(initial_4x, initial_4y, initial_4z, initial_4x, initial_4y, initial_4z + height, delay, steps=20) #up
            self.creepy_pod.legs[4].draw_straight_line(initial_4x, initial_4y, initial_4z + height, initial_4x, initial_4y + length, initial_4z + height, delay, steps=20) #forward
            self.creepy_pod.legs[4].draw_straight_line(initial_4x, initial_4y + length, initial_4z + height, initial_4x, initial_4y + length, initial_4z, delay, steps=20) #down
            time.sleep(3*delay*20)
            self.creepy_pod.legs[4].draw_straight_line(initial_4x, initial_4y + length, initial_4z, initial_4x, initial_4y, initial_4z, delay, steps=20) #back

    


        def move_leg5():
            time.sleep(3*delay*20)
            self.creepy_pod.legs[5].draw_straight_line(initial_5x, initial_5y, initial_5z, initial_5x, initial_5y, initial_5z + height, delay, steps=20) #up
            self.creepy_pod.legs[5].draw_straight_line(initial_5x, initial_5y, initial_5z + height, initial_5x, initial_5y + length, initial_5z + height, delay, steps=20) # forward
            self.creepy_pod.legs[5].draw_straight_line(initial_5x, initial_5y + length, initial_5z + height, initial_5x, initial_5y + length, initial_5z, delay, steps=20) #down
            time.sleep(3*delay*20)
            self.creepy_pod.legs[5].draw_straight_line(initial_5x, initial_5y + length, initial_5z, initial_5x, initial_5y, initial_5z, delay, steps=20) # back
            time.sleep(2*delay*20)
            self.creepy_pod.legs[5].draw_straight_line(initial_5x, initial_5y, initial_5z, initial_5x, initial_5y, initial_5z + height, delay, steps=20) #up
            self.creepy_pod.legs[5].draw_straight_line(initial_5x, initial_5y, initial_5z + height, initial_5x, initial_5y + length, initial_5z + height, delay, steps=20) # forward
            self.creepy_pod.legs[5].draw_straight_line(initial_5x, initial_5y + length, initial_5z + height, initial_5x, initial_5y + length, initial_5z, delay, steps=20) #down
            self.creepy_pod.legs[5].draw_straight_line(initial_5x, initial_5y + length, initial_5z, initial_5x, initial_5y, initial_5z, delay, steps=20) # back


        # Create threads for each leg
        thread0 = threading.Thread(target=move_leg0)
        thread1 = threading.Thread(target=move_leg1)
        thread2 = threading.Thread(target=move_leg2)
        thread3 = threading.Thread(target=move_leg3)
        thread4 = threading.Thread(target=move_leg4)
        thread5 = threading.Thread(target=move_leg5)

        # Start the threads
        thread0.start()
        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
        thread5.start()

        # Wait for all threads to complete
        thread0.join()
        thread1.join()
        thread2.join()
        thread3.join()
        thread4.join()
        thread5.join()


    def ripple_rotate_left(self, 
                                    initial_0x, initial_0y, initial_0z,
                                    initial_1x, initial_1y, initial_1z,
                                    initial_2x, initial_2y, initial_2z, 
                                    initial_3x, initial_3y, initial_3z, 
                                    initial_4x, initial_4y, initial_4z, 
                                    initial_5x, initial_5y, initial_5z, length, height, delay):
        def move_leg0():
            #step 1
            time.sleep(3*delay*20)
            #step 2
            self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y, initial_0z, initial_0x, initial_0y + length, initial_0z, delay, steps=20) # forward
            time.sleep(2*delay*20) 
            #step 3
            self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y + length, initial_0z, initial_0x, initial_0y + length, initial_0z + height, delay, steps=20) # up
            self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y + length, initial_0z + height, initial_0x, initial_0y, initial_0z + height, delay, steps=20) # back
            self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y, initial_0z + height, initial_0x, initial_0y, initial_0z, delay, steps=20) # down
            #step 4
            self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y, initial_0z, initial_0x, initial_0y + length, initial_0z, delay, steps=20) # forward
            time.sleep(2*delay*20)
            #step 5
            time.sleep(3*delay*20)
            #step 6
            self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y + length, initial_0z, initial_0x, initial_0y + length, initial_0z + height, delay, steps=20) # up
            self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y + length, initial_0z + height, initial_0x, initial_0y, initial_0z + height, delay, steps=20) # back
            self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y, initial_0z + height, initial_0x, initial_0y, initial_0z, delay, steps=20) # down


        def move_leg1():
            #step 1
            self.creepy_pod.legs[1].draw_straight_line(initial_1x, initial_1y + length, initial_1z, initial_1x, initial_1y + length, initial_1z + height, delay, steps=20) # up
            self.creepy_pod.legs[1].draw_straight_line(initial_1x, initial_1y + length, initial_1z + height, initial_1x, initial_1y, initial_1z + height, delay, steps=20) # back
            self.creepy_pod.legs[1].draw_straight_line(initial_1x, initial_1y, initial_1z + height, initial_1x, initial_1y, initial_1z, delay , steps=20) # down
            #step 2
            self.creepy_pod.legs[1].draw_straight_line(initial_1x, initial_1y, initial_1z, initial_1x, initial_1y + length, initial_1z, delay, steps=20) # forward
            self.creepy_pod.legs[1].draw_straight_line(initial_1x, initial_1y + length, initial_1z, initial_1x, initial_1y + length, initial_1z + height, delay, steps=20) #up
            self.creepy_pod.legs[1].draw_straight_line(initial_1x, initial_1y + length, initial_1z + height, initial_1x, initial_1y, initial_1z + height, delay, steps=20) #back
            self.creepy_pod.legs[1].draw_straight_line(initial_1x, initial_1y, initial_1z + height, initial_1x, initial_1y, initial_1z, delay, steps=20) #down
            #step 2
            self.creepy_pod.legs[1].draw_straight_line(initial_1x, initial_1y, initial_1z, initial_1x, initial_1y + length, initial_1z, delay, steps=20) #forward
            time.sleep(2*delay*20)
            #step 3
            time.sleep(3*delay*20)
            #step 4
            self.creepy_pod.legs[1].draw_straight_line(initial_1x, initial_1y + length, initial_1z, initial_1x, initial_1y + length, initial_1z + height, delay, steps=20) # up
            self.creepy_pod.legs[1].draw_straight_line(initial_1x, initial_1y + length, initial_1z + height, initial_1x, initial_1y, initial_1z + height, delay, steps=20) # back
            self.creepy_pod.legs[1].draw_straight_line(initial_1x, initial_1y, initial_1z + height, initial_1x, initial_1y, initial_1z, delay , steps=20) # down
            #step 5
            time.sleep(3*delay*20)
            #step 6
            self.creepy_pod.legs[1].draw_straight_line(initial_1x, initial_1y, initial_1z, initial_1x, initial_1y + length, initial_1z, delay, steps=20) # forward
            time.sleep(2*delay*20)

        def move_leg2():
            #step 1
            time.sleep(3*delay*20)
            #step 2
            self.creepy_pod.legs[2].draw_straight_line(initial_2x, initial_2y + length, initial_2z, initial_2x, initial_2y + length, initial_2z + height, delay, steps=20) #up
            self.creepy_pod.legs[2].draw_straight_line(initial_2x, initial_2y + length, initial_2z + height, initial_2x, initial_2y, initial_2z + height, delay, steps=20) #back
            self.creepy_pod.legs[2].draw_straight_line(initial_2x, initial_2y, initial_2z + height, initial_2x, initial_2y , initial_2z, delay, steps=20) #down
            #step 3
            time.sleep(3*delay*20)
            #step 4
            self.creepy_pod.legs[2].draw_straight_line(initial_2x, initial_2y, initial_2z, initial_2x, initial_2y + length, initial_2z, delay, steps=20) #forward
            time.sleep(2*delay*20)
            #step 5
            self.creepy_pod.legs[2].draw_straight_line(initial_2x, initial_2y + length, initial_2z, initial_2x, initial_2y + length, initial_2z + height, delay, steps=20) #up
            self.creepy_pod.legs[2].draw_straight_line(initial_2x, initial_2y + length, initial_2z + height, initial_2x, initial_2y, initial_2z + height, delay, steps=20) #back
            self.creepy_pod.legs[2].draw_straight_line(initial_2x, initial_2y, initial_2z + height, initial_2x, initial_2y , initial_2z, delay, steps=20) #down
            #step 6
            self.creepy_pod.legs[2].draw_straight_line(initial_2x, initial_2y, initial_2z, initial_2x, initial_2y + length, initial_2z, delay, steps=20) #forward
            time.sleep(2*delay*20)

        def move_leg3():
            #step 1
            time.sleep(3*delay*20)
            #step 2
            self.creepy_pod.legs[3].draw_straight_line(initial_3x, initial_3y + length, initial_3z, initial_3x, initial_3y, initial_3z, delay, steps=20) #back
            time.sleep(2*delay*20)
            #step 3
            self.creepy_pod.legs[3].draw_straight_line(initial_3x, initial_3y, initial_3z, initial_3x, initial_3y, initial_3z + height, delay, steps=20) #up
            self.creepy_pod.legs[3].draw_straight_line(initial_3x, initial_3y, initial_3z + height, initial_3x, initial_3y + length, initial_3z + height, delay, steps=20) #forward
            self.creepy_pod.legs[3].draw_straight_line(initial_3x, initial_3y + length, initial_3z + height, initial_3x, initial_3y + length, initial_3z, delay, steps=20) #down
            #step 4
            self.creepy_pod.legs[3].draw_straight_line(initial_3x, initial_3y + length, initial_3z, initial_3x, initial_3y, initial_3z, delay, steps=20) #back
            time.sleep(2*delay*20)
            #step 5
            time.sleep(3*delay*20)
            #step 6
            self.creepy_pod.legs[3].draw_straight_line(initial_3x, initial_3y, initial_3z, initial_3x, initial_3y, initial_3z + height, delay, steps=20) #up
            self.creepy_pod.legs[3].draw_straight_line(initial_3x, initial_3y, initial_3z + height, initial_3x, initial_3y + length, initial_3z + height, delay, steps=20) #forward
            self.creepy_pod.legs[3].draw_straight_line(initial_3x, initial_3y + length, initial_3z + height, initial_3x, initial_3y + length, initial_3z, delay, steps=20) #down

        def move_leg4():
            #step 1
            self.creepy_pod.legs[4].draw_straight_line(initial_4x, initial_4y, initial_4z, initial_4x, initial_4y, initial_4z + height, delay, steps=20) #up 
            self.creepy_pod.legs[4].draw_straight_line(initial_4x, initial_4y, initial_4z + height, initial_4x, initial_4y + length, initial_4z + height, delay, steps=20) #forward
            self.creepy_pod.legs[4].draw_straight_line(initial_4x, initial_4y + length, initial_4z + height, initial_4x, initial_4y + length, initial_4z, delay, steps=20) #down
            #step 2
            self.creepy_pod.legs[4].draw_straight_line(initial_4x, initial_4y + length, initial_4z, initial_4x, initial_4y, initial_4z, delay, steps=20) #back
            time.sleep(2*delay*20)
            #step 3
            time.sleep(3*delay*20)
            #step 4
            self.creepy_pod.legs[4].draw_straight_line(initial_4x, initial_4y, initial_4z, initial_4x, initial_4y, initial_4z + height, delay, steps=20) #up
            self.creepy_pod.legs[4].draw_straight_line(initial_4x, initial_4y, initial_4z + height, initial_4x, initial_4y + length, initial_4z + height, delay, steps=20) #forward
            self.creepy_pod.legs[4].draw_straight_line(initial_4x, initial_4y + length, initial_4z + height, initial_4x, initial_4y + length, initial_4z, delay, steps=20) #down
            #step 5
            time.sleep(3*delay*20)
            #step 6
            self.creepy_pod.legs[4].draw_straight_line(initial_4x, initial_4y + length, initial_4z, initial_4x, initial_4y, initial_4z, delay, steps=20) #back
            time.sleep(2*delay*20)

        def move_leg5():
            #step 1
            time.sleep(3*delay*20)
            #step 2
            self.creepy_pod.legs[5].draw_straight_line(initial_5x, initial_5y, initial_5z, initial_5x, initial_5y, initial_5z + height, delay, steps=20) #up
            self.creepy_pod.legs[5].draw_straight_line(initial_5x, initial_5y, initial_5z + height, initial_5x, initial_5y + length, initial_5z + height, delay, steps=20) #forward
            self.creepy_pod.legs[5].draw_straight_line(initial_5x, initial_5y + length, initial_5z + height, initial_5x, initial_5y + length, initial_5z, delay, steps=20) #down
            #step 3
            time.sleep(3*delay*20)
            #step 4
            self.creepy_pod.legs[5].draw_straight_line(initial_5x, initial_5y + length, initial_5z, initial_5x, initial_5y, initial_5z, delay, steps=20) #back
            time.sleep(2*delay*20)
            #step 5
            self.creepy_pod.legs[5].draw_straight_line(initial_5x, initial_5y, initial_5z, initial_5x, initial_5y, initial_5z + height, delay, steps=20) #up
            self.creepy_pod.legs[5].draw_straight_line(initial_5x, initial_5y, initial_5z + height, initial_5x, initial_5y + length, initial_5z + height, delay, steps=20) #forward
            self.creepy_pod.legs[5].draw_straight_line(initial_5x, initial_5y + length, initial_5z + height, initial_5x, initial_5y + length, initial_5z, delay, steps=20) #down
            #step 6
            self.creepy_pod.legs[5].draw_straight_line(initial_5x, initial_5y + length, initial_5z, initial_5x, initial_5y, initial_5z, delay, steps=20) #back
            time.sleep(2*delay*20)

        # Create threads for each leg
        thread0 = threading.Thread(target=move_leg0)
        thread1 = threading.Thread(target=move_leg1)
        thread2 = threading.Thread(target=move_leg2)
        thread3 = threading.Thread(target=move_leg3)
        thread4 = threading.Thread(target=move_leg4)
        thread5 = threading.Thread(target=move_leg5)

        # Start the threads
        thread0.start()
        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
        thread5.start()

        # Wait for all threads to complete
        thread0.join()
        thread1.join()
        thread2.join()
        thread3.join()
        thread4.join()
        thread5.join()

    def draw_straight_line_three_legs(self, 
                                    initial_0x, initial_0y, initial_0z,
                                    initial_1x, initial_1y, initial_1z,
                                    initial_2x, initial_2y, initial_2z, length, height):
        def move_leg0():
            self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y, initial_0z, initial_0x, initial_0y + length, initial_0z, delay, steps=20)
            time.sleep(0.5)
            self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y + length, initial_0z, initial_0x, initial_0y + length, initial_0z + height, delay, steps=20)
            time.sleep(0.5)
            self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y + length, initial_0z + height, initial_0x, initial_0y, initial_0z + height, delay, steps=20)
            time.sleep(0.5)
            self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y, initial_0z + height, initial_0x, initial_0y, initial_0z, delay, steps=20)
            time.sleep(0.5)

        def move_leg1():
#            self.creepy_pod.legs[1].draw_straight_line(initial_1x, initial_1y, initial_1z, initial_1x, initial_1y - length, initial_1z, delay, steps=20)
#            time.sleep(2)
#            self.creepy_pod.legs[1].draw_straight_line(initial_1x, initial_1y - length, initial_1z, initial_1x, initial_1y - length, initial_1z-height, delay, steps=20)
#            time.sleep(4)
#            self.creepy_pod.legs[1].draw_straight_line(initial_1x, initial_1y - length, initial_1z-height, initial_1x, initial_1y, initial_1z-height, delay, steps=20)
#            time.sleep(4)
#            self.creepy_pod.legs[1].draw_straight_line(initial_1x, initial_1y, initial_1z-height, initial_1x, initial_1y, initial_1z, delay, steps=20)
            time.sleep(2)

        def move_leg2():
#            self.creepy_pod.legs[2].draw_straight_line(initial_2x, initial_2y, initial_2z, initial_2x, initial_2y + length, initial_2z, delay, steps=20)
#            time.sleep(4)
#            self.creepy_pod.legs[2].draw_straight_line(initial_2x, initial_2y + length, initial_2z, initial_2x, initial_2y + length, initial_2z + height, delay, steps=20)
#            time.sleep(2)
#            self.creepy_pod.legs[2].draw_straight_line(initial_2x, initial_2y + length, initial_2z + height, initial_2x, initial_2y, initial_2z + height, delay, steps=20)
#            time.sleep(2)
#            self.creepy_pod.legs[2].draw_straight_line(initial_2x, initial_2y, initial_2z + height, initial_2x, initial_2y, initial_2z, delay, steps=20)
            time.sleep(2)



        # Create threads for each leg
        thread0 = threading.Thread(target=move_leg0)
        thread1 = threading.Thread(target=move_leg1)
        thread2 = threading.Thread(target=move_leg2)
        # Start the threads
        thread0.start()
        thread1.start()
        thread2.start()
        # Wait for all threads to complete
        thread0.join()
        thread1.join()
        thread2.join()






    def draw_straight_line_two_legs_backup(self):
        def move_leg0():
            self.creepy_pod.legs[0].draw_straight_line(175, 200, -150, 175, 300, -150, delay, steps=20)
            time.sleep(2)
            self.creepy_pod.legs[0].draw_straight_line(175, 300, -150, 175, 300, -100, delay, steps=20)
            time.sleep(2)
            self.creepy_pod.legs[0].draw_straight_line(175, 300, -100, 175, 200, -100, delay, steps=20)
            time.sleep(2)
            self.creepy_pod.legs[0].draw_straight_line(175, 200, -100, 175, 200, -150, delay, steps=20)
            time.sleep(2)



        def move_leg2():
            self.creepy_pod.legs[2].draw_straight_line(175, -300, -150, 175, -200, -150, delay, steps=20)
            time.sleep(2)
            self.creepy_pod.legs[2].draw_straight_line(175, -200, -150, 175, -200, -100, delay, steps=20)
            time.sleep(2)
            self.creepy_pod.legs[2].draw_straight_line(175, -200, -100, 175, -300, -100, delay, steps=20)
            time.sleep(2)
            self.creepy_pod.legs[2].draw_straight_line(175, -300, -100, 175, -300, -150, delay, steps=20)
            time.sleep(2)

        def move_leg4():
            self.creepy_pod.legs[4].draw_straight_line(-425, -50, -150, -425, 50, -150, delay, steps=20)
            time.sleep(2)
            self.creepy_pod.legs[4].draw_straight_line(-425, 50, -150, -425, 50, -100, delay, steps=20)
            time.sleep(2)
            self.creepy_pod.legs[4].draw_straight_line(-425, 50, -100, -425, -50, -100, delay, steps=20)
            time.sleep(2)
            self.creepy_pod.legs[4].draw_straight_line(-425, -50, -100, -425, -50, -150, delay, steps=20)
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
