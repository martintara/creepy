# src
Most relevant files and classes for insight into the system:

# leg.py
```python
from servo import Servo
from maestro import Controller

class Leg:
    def __init__(self, controller: Controller, leg_id: int, servo_0: int, servo_1:int, servo_2:int):
        self.leg_id = leg_id  # Unique identifier for the leg
        self.servo_0 = Servo(controller, servo_0, 3450, 8600)
        self.servo_1 = Servo(controller, servo_1, 2700, 10100)
        self.servo_2 = Servo(controller, servo_2, 1650, 8600)

    def lower_leg(self):
        # self.servo_0.move(1474) #commented out while testing
        self.servo_1.move(8250)
        self.servo_2.move(6400)

    def initial_position(self):
        self.servo_0.move(int((self.servo_0.max_pos+self.servo_0.min_pos)/2))
        self.servo_1.move(self.servo_1.max_pos)
        self.servo_2.move(self.servo_2.max_pos)

```

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

from creepy_pod import CreepyPod
from creepy_state import CreepyState
from maestro import Controller
import maestro
from leg import Leg
import time

from servo import Servo

def main():
    # testing av leg objekter, har testet leg 0 og 1)
    ctrl = maestro.Controller()
    leg1 = Leg(ctrl, 1, 3, 4, 5)
    leg1.initial_position()
    time.sleep(5)
    leg1.lower_leg()
    time.sleep(5)
    leg1.initial_position()


# gammel kode:
"""
    servo = Servo(ctrl, 0, 2000, 5950) # creating servo object 2000min pos, 5950 max pos
    servo2 = Servo(ctrl, 1, 3950, 6900) # creating servo object 2000min pos, 5950 max pos
    servo3 = Servo(ctrl, 2, 4000, 7550) # creating servo object 2000min pos, 5950 max pos

    servo.move(2000)
    servo2.move(3950)
    servo3.move(4000)
    ctrl.close()

    leg0 = Leg(ctrl, 0, 0, 1, 2)
    leg0.lift_leg()

    creepy_pod = CreepyPod()
    creepy_pod.display_state()
    creepy_pod.change_state(CreepyState.IDLE)
    creepy_pod.display_state()
"""
if __name__ == "__main__":
    main()
```
