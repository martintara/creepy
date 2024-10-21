# generert på chat gpt - ikke implementert korrekt enda

# leg.py
from servo import Servo
from maestro import Controller

class Leg:
    def __init__(self, controller: Controller, leg_id: int, servo_0: int, servo_1:int, servo_2:int):
        self.leg_id = leg_id  # Unique identifier for the leg
        self.servo_0 = Servo(controller, servo_0, 3550, 8250)
        self.servo_1 = Servo(controller, servo_1, 2350, 9900)
        self.servo_2 = Servo(controller, servo_2, 1600, 8100)

    def lower_leg(self):
        # self.servo_0.move(1474)
        self.servo_1.move(8000)
        self.servo_2.move(6000)

    def initial_position(self):
        self.servo_0.move(int((self.servo_0.max_pos+self.servo_0.min_pos)/2.0))
        self.servo_1.move(self.servo_1.max_pos)
        self.servo_2.move(self.servo_2.max_pos)

