# leg.py
from servo import Servo
from maestro import Controller
import math
import time

class Leg:
    def __init__(self, leg_id: int, servo_params, ctrl: Controller, offset=0):
        self.leg_id = leg_id  # Unique identifier for the leg
        self.offset = offset
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
        # Constants in millimeters
        Z_offset = 10.2     # Vertical offset between innermost and middle servos
        r1 = 45             # Fixed horizontal distance from innermost to middle servo
        a2 = 149.5          # Length of the middle arm
        a3 = 213.66         # Length of the outer arm

        # Step 1: Adjust the target z-coordinate relative to the middle servo
        z_adjusted = z - Z_offset

        # Step 2: Calculate theta1 (horizontal rotation angle) and add the leg-specific offset
        theta1 = math.degrees(math.atan2(y, x)) + self.offset

        # Step 3: Calculate r_horizontal (effective horizontal distance in the x-y plane)
        r_horizontal = math.sqrt(x**2 + y**2)

        # Step 4: Calculate r4 (horizontal distance from middle servo to endpoint)
        r4 = r_horizontal - r1

        # Step 5: Calculate r2 (vertical distance from the horizontal line at the middle servo to the endpoint)
        r2 = z_adjusted

        # Step 6: Calculate r3 (distance from middle servo to endpoint)
        r3 = math.sqrt(r2**2 + r4**2)

        # Step 7: Calculate phi2 (angle between the middle arm and the line to the endpoint), with clamping
        phi2_value = (a2**2 + r3**2 - a3**2) / (2 * a2 * r3)
        phi2_value = max(-1, min(1, phi2_value))  # Clamp to the range [-1, 1]
        phi2 = math.degrees(math.acos(phi2_value))

        # Step 8: Calculate alpha (angle between the horizontal line and r3)
        alpha = math.degrees(math.atan2(r2, r4))

        # Step 9: Calculate theta2 with horizontal as 0 degrees and anti-clockwise as positive
        theta2 = alpha + phi2

        # Step 10: Calculate phi3 (internal angle between the middle arm and the outer arm), with clamping
        phi3_value = (r3**2 - a2**2 - a3**2) / (-2 * a2 * a3)
        phi3_value = max(-1, min(1, phi3_value))  # Clamp to the range [-1, 1]
        phi3 = math.degrees(math.acos(phi3_value))

        # Step 11: Calculate theta3, with negative values lifting the arm and positive values lowering it
        theta3 = 90 - phi3

        return theta1, theta2, theta3

    def move_parallel(self, x_global, y_start, distance, z, step=5):
        """
        Moves the leg along a line parallel to the global x-axis from y_start 
        by a specified distance, using an internal step size.

        Parameters:
        x_global (float): The fixed x-coordinate in the global coordinate system.
        y_start (float): The starting y-coordinate in the global coordinate system.
        distance (float): The distance to move along the y-axis (positive or negative).
        z (float): The fixed z-coordinate.
        step (float): The incremental step size in the y-direction (default is 5).
        """
        # Determine the end y-position
        y_end = y_start + distance

        # Determine the direction and number of steps
        y_direction = 1 if y_end > y_start else -1
        num_steps = abs(y_end - y_start) // step

        # Loop to move from start to end in increments of `step`
        for i in range(num_steps + 1):
            # Calculate the current global y position
            y_global = y_start + i * step * y_direction

            # Transform the global (x, y) coordinates to the leg’s local coordinates
            x_local = x_global * math.cos(math.radians(self.offset)) - y_global * math.sin(math.radians(self.offset))
            y_local = x_global * math.sin(math.radians(self.offset)) + y_global * math.cos(math.radians(self.offset))

            # Move the leg to the transformed local coordinates
            self.move_to_coordinates(x_local, y_local, z)
            time.sleep(0.1)
