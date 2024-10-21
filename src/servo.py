# servo.py
from maestro import Controller # neccessary to be able to pass controller object

class Servo:
    """
    Class that controls position, speed and acceleration of a servo motor.

    Attributes:
    -----------
    channel: int
        ID number (and corresponding pin number) of unique servo.
    controller: Controller
        controller object passed from elsewhere in the system
    position: int
        Last given position of servo.
    min_pos: int
        Minimum position the servo is allowed to use. Used to restrict the servo to operate within safe range.
    max_pos: int
        Maximum position the servo is allowed to use. Used to restrict the servo to operate within safe range.

    Methods:
    -----------
    move(position)
        Moves servo to given position.
    """
    def __init__(self, controller: Controller, channel: int, min: int, max: int):
        self.channel = channel 
        self.controller = controller
        self.position = 0  # default start position
        self.min_pos = min
        self.max_pos = max
        self.speed = 25 # default speed
        self.acceleration = 25 # default acceleration

    def move(self, position: int):
        self.position = position
        self.controller.setRange(self.channel, self.min_pos, self.max_pos)
        self.controller.setAccel(self.channel, self.acceleration)
        self.controller.setSpeed(self.channel, self.speed)
        self.controller.setTarget(self.channel, position)
        print(f"Servo {self.channel} moved to position {self.position}")

    def setAcceleration(self, acceleration: int):
        self.acceleration = acceleration

    def setSpeed(self, speed: int):
        self.speed = speed
