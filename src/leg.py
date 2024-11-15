# leg.py
from servo import Servo
from maestro import Controller
import math
import time

class Leg:
    def __init__(self, leg_id: int, servo_params, ctrl: Controller, origin_x, origin_y, offset=0):
        self.leg_id = leg_id  # Unique identifier for the leg
        self.offset = offset
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.servos = [Servo(ctrl, **params) for params in servo_params]  # Initialize servos for the leg
    def lower_leg(self):
        self.servos[1].move_to_angle(57)

        self.servos[2].move_to_angle(40)

    def rise_leg(self):
        self.servos[1].move_to_angle(90)



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

    def leg_forward(self):
        """Move leg forward, adjusted for orientation."""
        # Move to max_pos for forward if offset is in [315, 45, 225, 135]
        if self.offset in [315, 45, 0]:
            forward_position = self.servos[0].max_pos
        else:
            # Otherwise, move to min_pos for forward (center legs with offsets 0 and 180)
            forward_position = self.servos[0].min_pos

        self.servos[0].move(forward_position)
        print(f"Leg {self.leg_id} moved forward with orientation offset {self.offset}, "
              f"minpos {self.servos[0].min_pos}, maxpos {self.servos[0].max_pos}")


    def leg_backward(self):
        """Move leg backward, adjusted for orientation."""
        backward_position = self.servos[0].min_pos if self.offset in [315, 45, 0] else self.servos[0].max_pos
        self.servos[0].move(backward_position)
        print(f"Leg {self.leg_id} moved backward with orientation offset {self.offset}")

    def manual_control(self, id: int):
        self.servos[id].manual_control()

    def manual_control_angle(self, id: int):
        self.servos[id].manual_control_angle()

    def move_to_coordinates(self, x, y, z):
        theta1, theta2, theta3 = self.calculate_angles(x, y, z)
        self.servos[0].move_to_angle(theta1)
        self.servos[1].move_to_angle(theta2)
        self.servos[2].move_to_angle(theta3)

    def calculate_angles(self, x, y, z):
        # Constants for the arm segments
        Z_offset = -10.2  # cm (vertical segment positioned below the base)
        horizontal_offset = 45   # cm (horizontal segment after the 90-degree bend)
        a2 = 149.5  # cm (distance from second servo to outermost servo)
        a3 = 213.66  # cm (distance from outermost servo to end effector)

        # Calculate theta1 based on target (x, y)
        theta1 = math.degrees(math.atan2(y, x))
        
        # Adjusted coordinates for target relative to the second servo
        effective_x = x - horizontal_offset
        r1 = math.sqrt(effective_x**2 + y**2)
        
        # Calculate effective r2 as the Z distance from the second servo’s height (below the base)
        r2 = z - Z_offset  # Since vertical_segment is negative, this adds 10 to Z

        # Calculate phi2
        phi2 = math.degrees(math.atan2(r2, r1))
        
        # Calculate r3
        r3 = math.sqrt(r1**2 + r2**2)
        
        # Ensure r3 is within range to avoid math domain errors in acos
        phi1 = math.degrees(math.acos(max(min((a3**2 - a2**2 - r3**2) / (-2 * a2 * r3), 1), -1)))
        phi3 = math.degrees(math.acos(max(min((r3**2 - a2**2 - a3**2) / (-2 * a2 * a3), 1), -1)))
        
        # Calculate theta2 and theta3
        theta2 = phi2 + phi1
        theta3 = 90 - phi3 #-(180 - phi3) + 90

        print(f"theta1:{theta1},theta2: {theta2} , theta3 {theta3}")

 


    def print_offsets(self):
        print(f"{self.offset},origin_x: {self.origin_x} , origin_y {self.origin_y}")
