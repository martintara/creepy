    def draw_straight_line_two_legs(self):

        def move_leg0():
            self.creepy_pod.legs[0].draw_straight_line(175, 200, -150, 175, 300, -150, steps=20)
            time.sleep(2)
            self.creepy_pod.legs[0].draw_straight_line(175, 300, -150, 175, 300, -100, steps=20)
            time.sleep(2)
            self.creepy_pod.legs[0].draw_straight_line(175, 300, -100, 175, 200, -100, steps=20)
            time.sleep(2)
            self.creepy_pod.legs[1].draw_straight_line(175, 200, -100, 175, 200, -150, steps=20)
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



       def move_leg0():
           self.creepy_pod.legs[0].draw_straight_line(inital_0x, initial_0y, initial_0z, initial_0x, initial_0y + 100, initial_0z, steps=20)
           time.sleep(2)
           self.creepy_pod.legs[0].draw_straight_line(inital_0x, initial_0y + 100, initial_0z, initial_0x, initial_0y + 100, initial_0z+50, steps=20)
           time.sleep(2)
           self.creepy_pod.legs[0].draw_straight_line(inital_0x, initial_0y + 100, initial_0z+50, initial_0x, initial_0y, initial_0z+50, steps=20)
           time.sleep(2)
           self.creepy_pod.legs[0].draw_straight_line(initial_0x, initial_0y, initial_0z+50, initial_0x, initial_0y, initial_0z, steps=20)
           time.sleep(2)