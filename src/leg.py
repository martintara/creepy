# leg.py
from servo import Servo
from maestro import Controller

class Leg:
    def __init__(self, controller: Controller, leg_id: int, servo_0: int, servo_1:int, servo_2:int, servo_0_min:int, servo_0_max:int, servo_1_min:int, servo_1_max:int, servo_2_min:int, servo_2_max:int,):
        self.leg_id = leg_id  # Unique identifier for the leg
        self.servo_0 = Servo(controller, servo_0, servo_0_min, servo_0_max)
        self.servo_1 = Servo(controller, servo_1, servo_1_min, servo_1_max)
        self.servo_2 = Servo(controller, servo_2, servo_2_min, servo_2_max)

    def lower_leg(self):
        # self.servo_0.move(1474) #commented out while testing
        self.servo_1.move(int(((((self.servo_1.max_pos+self.servo_1.min_pos)/2)+self.servo_1.max_pos))/2))
        self.servo_2.move(int((self.servo_2.max_pos+self.servo_2.min_pos)/1.6))

    def initial_position(self):
        self.servo_0.move(int((self.servo_0.max_pos+self.servo_0.min_pos)/2))
        self.servo_1.move(self.servo_1.max_pos)
        self.servo_2.move(self.servo_2.max_pos)

