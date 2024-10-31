# leg.py
from servo import Servo
from maestro import Controller

class Leg:
    def __init__(self, controller: Controller, leg_id: int, servos: list[Servo]):
        self.leg_id = leg_id  # Unique identifier for the leg
        self.servos = servos

    def standby_position(self):
        # self.servo_0.move(1474) #commented out while testing
#       self.servos[1].move(int(((((self.servos[1].max_pos+self.servos[1].min_pos)/2)+self.servos[1].max_pos))/2))
        self.servos[1].move(int((self.servos[1].center_pos+self.servos[1].max_pos)/2))

#       self.servos[2].move(int((self.servos[2].max_pos+self.servos[2].min_pos)/1.6))
        self.servos[2].move(int((self.servos[2].center_pos*2)/1.6))

    def initial_position(self):
#       self.servos[0].move(int((self.servos[0].max_pos+self.servos[0].min_pos)/2))
        self.servos[0].move(self.servos[0].center_pos)
        self.servos[1].move(self.servos[1].max_pos)
        self.servos[2].move(self.servos[2].max_pos)

    def straight_up(self):
#       self.servos[0].move(int((self.servos[0].max_pos+self.servos[0].min_pos)/2))
#       self.servos[0].move(self.servos[0].center_pos)
        self.servos[1].move(self.servos[1].max_pos)
        self.servos[2].move(self.servos[2].min_pos)

    def straight_down(self):
#       self.servos[0].move(int((self.servos[0].max_pos+self.servos[0].min_pos)/2))
        self.servos[0].move(self.servos[0].center_pos)
        self.servos[1].move(self.servos[1].min_pos)
        self.servos[2].move(self.servos[2].min_pos)

    def manual_control(self, id: int):
        self.servos[id].manual_control()

    def rise_leg(self): 
        self.servos[1].move(self.servos[1].max_pos)
        self.servos[2].move(self.servos[2].max_pos)

    def lower_leg(self):
        #self.servos[0].move(self.servos[0].center_pos)
        self.servos[1].move(self.servos[1].center_pos)
        self.servos[2].move(int((self.servos[2].center_pos)*0.9))

    def rotate_forward(self):
        self.servos[0].move(self.servos[0].max_pos)

    def rotate_backward(self):
        self.servos[0].move(self.servos[0].min_pos)

    def standby_position2(self):
        self.servos[1].move(int(((self.servos[1].max_pos)/10)*7))
        self.servos[2].move(int((self.servos[2].center_pos*2)/1.8))

       
