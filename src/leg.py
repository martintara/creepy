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

    def manual_control_ik(self)
        """
        Continuously takes input for coordinates (x, y, z), separated by commas.
        Calls move_to_coordinates(x, y, z) for each input.
        Enter 'q' to quit the loop.
        """
        while True:
            user_input = input("Enter coordinates (x, y, z) separated by commas, or 'q' to quit: ")
            if user_input.lower() == 'q':
                print("Exiting the loop.")
                break
            
            try:
                x, y, z = map(float, user_input.split(','))
                self.move_to_coordinates(x, y, z)
            except ValueError:
                print("Invalid input. Please enter three numbers separated by commas, or 'q' to quit.")   

    def rotate_coordinates(self, x, y):
        angle_radians = math.radians(self.offset)
        rotated_x = x * math.cos(angle_radians) + y * math.sin(angle_radians)
        rotated_y = -x * math.sin(angle_radians) + y * math.cos(angle_radians)
        return rotated_x, rotated_y

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

        return theta1, theta2, theta3

        def calculate_global_positions(self, x, y, z):
        Z_offset = -10.2  # cm
        horizontal_offset = 45  # cm
        a2 = 149.5  # cm
        a3 = 213.66  # cm

        # Global to local coordinate conversion
        x_adjusted = x - self.origin_x
        y_adjusted = y - self.origin_y
        x_local, y_local = self.rotate_coordinates(x_adjusted, y_adjusted)

        # Calculate angles
        theta1, theta2, theta3 = self.calculate_angles(x_local, y_local, z)

        print(f"theta1:{theta1},theta2: {theta2} , theta3 {theta3}")



    def calculate_angles_backup(self, x, y, z):
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

        return theta1, theta2, theta3
 

    def move_straight_line(self, start, end, steps=50, delay=0.05):
        """
        Move the end effector in a straight line from `start` to `end`.

        Parameters:
            start (tuple): Starting position (x, y, z) in the global frame.
            end (tuple): Ending position (x, y, z) in the global frame.
            steps (int): Number of steps to divide the movement into.
            delay (float): Delay in seconds between each step.
        """
        x1, y1, z1 = start
        x2, y2, z2 = end

        for i in range(steps + 1):
            # Interpolate between start and end positions
            x_global = x1 + (x2 - x1) * i / steps
            y_global = y1 + (y2 - y1) * i / steps
            z_global = z1 + (z2 - z1) * i / steps

            # Rotate to the leg's local coordinate system
            x_local, y_local = self.rotate_coordinates(x_global, y_global)

            # Calculate angles in the local frame
            theta1, theta2, theta3 = self.calculate_angles(x_local, y_local, z_global)

            # Move the servos
            self.servos[0].move_to_angle(theta1)
            self.servos[1].move_to_angle(theta2)
            self.servos[2].move_to_angle(theta3)

            # Delay between steps
            time.sleep(delay)


    # def move_straight_line(self, start, end, steps=50, delay=0.05, offset=0):
    #     """
    #     Moves the end effector in a straight line from `start` to `end` using
    #     `calculate_angles` to compute servo positions.

    #     Args:
    #         start (tuple): Starting position (x, y, z).
    #         end (tuple): Ending position (x, y, z).
    #         steps (int): Number of steps in the movement.
    #         delay (float): Delay in seconds between each step.
    #     """
    #     x1, y1, z1 = start
    #     x2, y2, z2 = end

    #     for i in range(steps + 1):
    #         # Interpolate between start and end positions
    #         x = x1 + (x2 - x1) * i / steps
    #         y = y1 + (y2 - y1) * i / steps
    #         z = z1 + (z2 - z1) * i / steps

    #         # Calculate angles for the current step
    #         theta1, theta2, theta3 = self.calculate_angles(x, y, z)

    #         # Print the angles (replace this with actual servo commands in your robot control system)
    #         self.servos[0].move_to_angle(theta1)
    #         self.servos[1].move_to_angle(theta2)
    #         self.servos[2].move_to_angle(theta3)
    #         # Wait for the delay
    #         time.sleep(delay)


    def print_offsets(self):
        print(f"{self.offset},origin_x: {self.origin_x} , origin_y {self.origin_y}")

    def rotate_coordinates(self, x, y):
        """
        Rotate global coordinates (x, y) to the leg's local frame based on its offset.

        Parameters:
            x (float): The x-coordinate in the global frame.
            y (float): The y-coordinate in the global frame.

        Returns:
            tuple: The rotated (x, y) coordinates in the leg's local frame.
        """
        angle_radians = math.radians(self.offset)
        rotated_x = x * math.cos(angle_radians) + y * math.sin(angle_radians)
        rotated_y = -x * math.sin(angle_radians) + y * math.cos(angle_radians)
        return rotated_x, rotated_y
