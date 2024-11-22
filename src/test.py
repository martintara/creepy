import time
delay = 0.01
# delay
# time.sleep("nr of cycles"*delay*20)
# forward
# self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y, initial_0z + height, initial_0x, initial_0y + length, initial_0z + height, delay, steps=20)
# back
# self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y + length, initial_0z, initial_0x, initial_0y, initial_0z, delay, steps=20) 
# up
# self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y, initial_0z, initial_0x, initial_0y, initial_0z + height, delay, steps=20)  
# down
# self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y + length, initial_0z + height, initial_0x, initial_0y + length, initial_0z, delay, steps=20) 
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
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y, initial_0z + height, initial_0x, initial_0y + length, initial_0z + height, delay, steps=20)
        time.sleep(2*delay*20) 
        #step 3
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y, initial_0z, initial_0x, initial_0y, initial_0z + height, delay, steps=20)
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y + length, initial_0z, initial_0x, initial_0y, initial_0z, delay, steps=20)
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y + length, initial_0z + height, initial_0x, initial_0y + length, initial_0z, delay, steps=20) 
        #step 4
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y, initial_0z + height, initial_0x, initial_0y + length, initial_0z + height, delay, steps=20)
        time.sleep(2*delay*20)
        #step 5
        time.sleep(3*delay*20)
        #step 6
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y, initial_0z, initial_0x, initial_0y, initial_0z + height, delay, steps=20)
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y + length, initial_0z, initial_0x, initial_0y, initial_0z, delay, steps=20)
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y + length, initial_0z + height, initial_0x, initial_0y + length, initial_0z, delay, steps=20) 

    def move_leg1():
        #step 1
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y, initial_0z, initial_0x, initial_0y, initial_0z + height, delay, steps=20)
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y + length, initial_0z, initial_0x, initial_0y, initial_0z, delay, steps=20)
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y + length, initial_0z + height, initial_0x, initial_0y + length, initial_0z, delay, steps=20)
        #step 2
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y, initial_0z + height, initial_0x, initial_0y + length, initial_0z + height, delay, steps=20)
        time.sleep(2*delay*20)
        #step 3
        time.sleep(3*delay*20)
        #step 4
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y, initial_0z, initial_0x, initial_0y, initial_0z + height, delay, steps=20)
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y + length, initial_0z, initial_0x, initial_0y, initial_0z, delay, steps=20)
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y + length, initial_0z + height, initial_0x, initial_0y + length, initial_0z, delay, steps=20)
        #step 5
        time.sleep(3*delay*20)
        #step 6
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y, initial_0z + height, initial_0x, initial_0y + length, initial_0z + height, delay, steps=20)
        time.sleep(2*delay*20)

    def move_leg2():
        #step 1
        time.sleep(3*delay*20)
        #step 2
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y, initial_0z, initial_0x, initial_0y, initial_0z + height, delay, steps=20)
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y + length, initial_0z, initial_0x, initial_0y, initial_0z, delay, steps=20)
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y + length, initial_0z + height, initial_0x, initial_0y + length, initial_0z, delay, steps=20)
        #step 3
        time.sleep(3*delay*20)
        #step 4
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y, initial_0z + height, initial_0x, initial_0y + length, initial_0z + height, delay, steps=20)
        time.sleep(2*delay*20)
        #step 5
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y, initial_0z, initial_0x, initial_0y, initial_0z + height, delay, steps=20)
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y + length, initial_0z, initial_0x, initial_0y, initial_0z, delay, steps=20)
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y + length, initial_0z + height, initial_0x, initial_0y + length, initial_0z, delay, steps=20)
        #step 6
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y, initial_0z + height, initial_0x, initial_0y + length, initial_0z + height, delay, steps=20)
        time.sleep(2*delay*20)

    def move_leg3():
        #step 1
        time.sleep(3*delay*20)
        #step 2
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y + length, initial_0z, initial_0x, initial_0y, initial_0z, delay, steps=20)
        time.sleep(2*delay*20)
        #step 3
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y, initial_0z, initial_0x, initial_0y, initial_0z + height, delay, steps=20)
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y, initial_0z + height, initial_0x, initial_0y + length, initial_0z + height, delay, steps=20)
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y + length, initial_0z + height, initial_0x, initial_0y + length, initial_0z, delay, steps=20)
        #step 4
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y + length, initial_0z, initial_0x, initial_0y, initial_0z, delay, steps=20)
        time.sleep(2*delay*20)
        #step 5
        time.sleep(3*delay*20)
        #step 6
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y, initial_0z, initial_0x, initial_0y, initial_0z + height, delay, steps=20)
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y, initial_0z + height, initial_0x, initial_0y + length, initial_0z + height, delay, steps=20)
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y + length, initial_0z + height, initial_0x, initial_0y + length, initial_0z, delay, steps=20)

    def move_leg4():
        #step 1
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y, initial_0z, initial_0x, initial_0y, initial_0z + height, delay, steps=20)
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y, initial_0z + height, initial_0x, initial_0y + length, initial_0z + height, delay, steps=20)
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y + length, initial_0z + height, initial_0x, initial_0y + length, initial_0z, delay, steps=20)
        #step 2
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y + length, initial_0z, initial_0x, initial_0y, initial_0z, delay, steps=20)
        time.sleep(2*delay*20)
        #step 3
        time.sleep(3*delay*20)
        #step 4
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y, initial_0z, initial_0x, initial_0y, initial_0z + height, delay, steps=20)
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y, initial_0z + height, initial_0x, initial_0y + length, initial_0z + height, delay, steps=20)
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y + length, initial_0z + height, initial_0x, initial_0y + length, initial_0z, delay, steps=20)
        #step 5
        time.sleep(3*delay*20)
        #step 6
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y + length, initial_0z, initial_0x, initial_0y, initial_0z, delay, steps=20)
        time.sleep(2*delay*20)

    def move_leg5():
        #step 1
        time.sleep(3*delay*20)
        #step 2
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y, initial_0z, initial_0x, initial_0y, initial_0z + height, delay, steps=20)
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y, initial_0z + height, initial_0x, initial_0y + length, initial_0z + height, delay, steps=20)
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y + length, initial_0z + height, initial_0x, initial_0y + length, initial_0z, delay, steps=20)
        #step 3
        time.sleep(3*delay*20)
        #step 4
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y + length, initial_0z, initial_0x, initial_0y, initial_0z, delay, steps=20)
        time.sleep(2*delay*20)
        #step 5
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y, initial_0z, initial_0x, initial_0y, initial_0z + height, delay, steps=20)
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y, initial_0z + height, initial_0x, initial_0y + length, initial_0z + height, delay, steps=20)
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y + length, initial_0z + height, initial_0x, initial_0y + length, initial_0z, delay, steps=20)
        #step 6
        self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y + length, initial_0z, initial_0x, initial_0y, initial_0z, delay, steps=20)
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