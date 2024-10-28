# leg.py
from servo import Servo
from maestro import Controller

class Leg:
    def __init__(self, controller: Controller, leg_id: int, servos: list[Servo]):
        self.leg_id = leg_id  # Unique identifier for the leg
        self.servos = servos

    def lower_leg(self):
        # self.servo_0.move(1474) #commented out while testing
        self.servos[1].move(int(((((self.servos[1].max_pos+self.servos[1].min_pos)/2)+self.servos[1].max_pos))/2))
        self.servos[2].move(int((self.servos[2].max_pos+self.servos[2].min_pos)/1.6))

    def initial_position(self):
        self.servos[0].move(int((self.servos[0].max_pos+self.servos[0].min_pos)/2))
        self.servos[1].move(self.servos[1].max_pos)
        self.servos[2].move(self.servos[2].max_pos)

