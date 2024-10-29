# src
Most relevant files and classes for insight into the system:

# leg.py
```python
from servo import Servo
from maestro import Controller

class Leg:
    def __init__(self, controller: Controller, leg_id: int, servos: list[Servo]):
        self.leg_id = leg_id  # Unique identifier for the leg
        self.servos = servos

    def lower_leg(self):
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
    max_pos: int
        Maximum position the servo is allowed to use. Used to restrict the servo to operate within safe range.

    Methods:
    -----------
    move(position)
        Moves servo to given position.
    """
    def __init__(self, controller: Controller, channel: int, center_pos: int, range: int, center_angle, angle_range):
        self.channel = channel 
        self.controller = controller
        self.center_pos = center_pos
        self.position = 0  # default start position
        self.min_pos = center_pos-range
        self.max_pos = center_pos+range
        self.min_angle = center_angle - angle_range
        self.max_angle = center_angle + angle_range
        self.speed = 25 # default speed
        self.acceleration = 25 # default acceleration

    def move(self, position: int):
        self.position = position
        self.controller.setRange(self.channel, self.min_pos, self.max_pos)
        self.controller.setAccel(self.channel, self.acceleration)
        self.controller.setSpeed(self.channel, self.speed)
        self.controller.setTarget(self.channel, position)
        print(f"Servo {self.channel} moved to position {self.position}")
        print(f"Angle {self.position_to_angle(self.position)}")

    def setAcceleration(self, acceleration: int):
        self.acceleration = acceleration

    def setSpeed(self, speed: int):
        self.speed = speed

    def angle_to_position(self, angle):
        """
        Converts an angle to the corresponding servo position.
        Ensures angle is clamped between min_angle and max_angle.
        """
        # Constrain the angle to within the servo's angle range
        angle = max(self.min_angle, min(self.max_angle, angle))

        # Map angle to position, using center as the midpoint
        position = ((angle - self.min_angle) / (self.max_angle - self.min_angle)) * \
                   (self.max_pos - self.min_pos) + self.min_pos
        return position

    def position_to_angle(self, position):
        """
        Converts a servo position to the corresponding angle.
        Ensures position is clamped between min_pos and max_pos.
        """
        # Constrain the position to within the servo's position range
        position = max(self.min_pos, min(self.max_pos, position))

        # Map position back to angle, using center as the midpoint
        angle = ((position - self.min_pos) / (self.max_pos - self.min_pos)) * \
                (self.max_angle - self.min_angle) + self.min_angle
        return angle



    def manual_control(self):
        print(f"Entering manual control for Servo {self.channel}.")
        print(f"Type a number between {self.min_pos} and {self.max_pos}, or 'q' to quit.")
        
        while True:
            user_input = input("Enter position: ")

            # Exit if user enters 'q'
            if user_input.lower() == 'q':
                print("Exiting manual control.")
                break

            # Try to convert input to an integer
            try:
                position = int(user_input)
                
                # Check if position is within bounds
                if self.min_pos <= position <= self.max_pos:
                    # Simulate writing the value to the servo
                    self.move(position)
                    #print(f"Position set to {position}")
                else:
                    print(f"Error: Position must be between {self.min_pos} and {self.max_pos}.")
            
            except ValueError:
                print("Invalid input. Please enter an integer.")
```

# leg0test.py
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
 
    servo_list0 = [
        Servo(ctrl, 0, 5900, 2350, 0, 45),
        Servo(ctrl, 1, 6125, 3775, 0, 45),
        Servo(ctrl, 2, 5100, 3000, 0, 70)
                    ]


    servo_list1 = [
        Servo(ctrl, 3, 6025, 2350, 90, 90),
        Servo(ctrl, 4, 6400, 3775, 90, 90),
        Servo(ctrl, 5, 5125, 3250, 90, 90)
                   ]

    servo_list2 = [
        Servo(ctrl, 6, 6400, 2350, 90, 90),
        Servo(ctrl, 7, 6450, 3775, 90, 90),
        Servo(ctrl, 8, 5050, 3250, 90, 90)
                   ]

    servo_list3 = [
        Servo(ctrl, 9, 5750, 2350, 90, 90),
        Servo(ctrl, 10, 5875, 3775, 90, 90),
        Servo(ctrl, 11, 5200, 3250, 90, 90)
            ]

    servo_list4 = [
        Servo(ctrl, 12, 5600, 2350, 90, 90),
        Servo(ctrl, 13, 6400, 3775, 90, 90),
        Servo(ctrl, 14, 5025, 3250, 90, 90)
                   ]

    servo_list5 = [
        Servo(ctrl, 15, 5000, 2350, 90, 90),
        Servo(ctrl, 16, 6250, 3775, 90, 90),
        Servo(ctrl, 17, 5025, 3250, 90, 90)
                   ]




    leg0 = Leg(ctrl, 0, servo_list0)
#   leg1 = Leg(ctrl, 1, servo_list1)
#   leg2 = Leg(ctrl, 2, servo_list2)
#   leg3 = Leg(ctrl, 3, servo_list3)
#   leg4 = Leg(ctrl, 4, servo_list4)
#   leg5 = Leg(ctrl, 5, servo_list5)

#    leg0.initial_position()

#   leg1.initial_position()
#   leg2.initial_position()
#   leg3.initial_position()
#   leg4.initial_position()
#   leg5.initial_position()

#    time.sleep(5)

#    leg0.lower_leg()

#   leg1.lower_leg()
#   leg2.lower_leg()
#   leg3.lower_leg()
#   leg4.lower_leg()
#   leg5.lower_leg()

 #   time.sleep(5)
 #   leg0.straight_up()

 #   time.sleep(5)
 #   leg0.straight_down()


 #   time.sleep(5)

#   leg0.initial_position()
#   leg1.initial_position()
#   leg2.initial_position()
#   leg3.initial_position()
#   leg4.initial_position()
#   leg5.initial_position()

    leg0.manual_control(2)
    leg0.manual_control(1)

if __name__ == "__main__":
    main()
```
