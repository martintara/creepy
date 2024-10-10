# src
Most relevant files and classes for insight into the system:

# servo.py
```python
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
    max_post: int
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
```

# main.py
```python
# main.py

from creepy_pod import CreepyPod
from creepy_state import CreepyState
# from maestro import Controller
# import maestro

# from servo import Servo

def main():
    """ testing av servo-objekter (testet! fungerer!)
    ctrl = maestro.Controller()

    servo = Servo(ctrl, 17, 2000, 5950) # creating servo object 2000min pos, 5950 max pos
    servo2 = Servo(ctrl, 16, 3950, 6900) # creating servo object 2000min pos, 5950 max pos
    servo3 = Servo(ctrl, 15, 4000, 7550) # creating servo object 2000min pos, 5950 max pos

    servo.move(5000)
    servo2.move(5000)
    servo3.move(5000)
    ctrl.close()
    """

    creepy_pod = CreepyPod()
    creepy_pod.display_state()
    creepy_pod.change_state(CreepyState.IDLE)
    creepy_pod.display_state()

if __name__ == "__main__":
    main()
```
