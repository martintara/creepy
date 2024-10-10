# servo.py
from maestro import Controller

class Servo:
    def __init__(self, controller: Controller, channel: int, min: int, max: int):
        self.channel = channel  # ID number (and pin number) of unique servo
        self.controller = controller # Storing instance of passed controller object
        self.position = 0  # Default position is 0
        self.min_pos = min
        self.max_pos = max
        self.speed = 25
        self.acceleration = 25

    def move(self, position: int):
        """Test av move funksjon."""
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
