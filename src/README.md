# src
Most relevant files and classes for insight into the system:

# leg.py
```python
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
    
    leg0 = Leg(ctrl, 0, 0, 1, 2, 3550, 8250, 2350, 9900, 1600, 8100)
    leg1 = Leg(ctrl, 1, 3, 4, 5, 3450, 8600, 2700, 10100, 1650, 8600)
    leg2 = Leg(ctrl, 2, 6, 7, 8, 4500, 8300, 2600, 10300, 1600, 8500)
    leg3 = Leg(ctrl, 3, 9, 10, 11, 3800, 7700, 2150, 9600, 1600, 8800)
    leg4 = Leg(ctrl, 4, 12, 13, 14, 3400, 7800, 2550, 10250, 1600, 8450)
    leg5 = Leg(ctrl, 5, 15, 16, 17, 3000, 7000, 2500, 10000, 1600, 8450)

    leg0.initial_position()
    leg1.initial_position()
    leg2.initial_position()
    leg3.initial_position()
    leg4.initial_position()
    leg5.initial_position()

    time.sleep(5)

    leg0.lower_leg()
    leg1.lower_leg()
    leg2.lower_leg()
    leg3.lower_leg()
    leg4.lower_leg()
    leg5.lower_leg()

    time.sleep(5)

    leg0.initial_position()
    leg1.initial_position()
    leg2.initial_position()
    leg3.initial_position()
    leg4.initial_position()
    leg5.initial_position()




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
