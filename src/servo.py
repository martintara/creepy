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
    def __init__(self, controller: Controller, channel: int, center_pos: int, range: int, center_angle, angle_range):
        self.channel = channel 
        self.controller = controller
        self.center_pos = center_pos
        self.position = 0  # default start position
        self.min_pos = center_pos-range
        self.max_pos = center_pos+range
        self.min_angle = center_angle - angle_range
        self.max_angle = center_angle + angle_range
        self.speed = 50 # default speed
        self.acceleration = 25 # default acceleration

    def move(self, position: int):
        self.position = position
        self.controller.setRange(self.channel, self.min_pos, self.max_pos)
        self.controller.setAccel(self.channel, self.acceleration)
        self.controller.setSpeed(self.channel, self.speed)
        self.controller.setTarget(self.channel, position)
        print(f"Servo {self.channel} moved to position {self.position}")
        print(f"Angle {self.position_to_angle(self.position)}")

    def move_to_angle(self, angle):
        self.move(int(self.angle_to_position(angle)))

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

    def manual_control_angle(self):
        print(f"Entering manual control for Servo {self.channel}.")
        print(f"Type a number between {self.min_angle} and {self.max_angle}, or 'q' to quit.")
        
        while True:
            user_input = input("Enter angle: ")

            # Exit if user enters 'q'
            if user_input.lower() == 'q':
                print("Exiting manual control.")
                break

            # Try to convert input to an integer
            try:
                angle = int(user_input)
                position = int(self.angle_to_position(angle))
                # Check if position is within bounds
                if self.min_angle <= angle <= self.max_angle:
                    # Simulate writing the value to the servo
                    self.move(position)
                    print(f"Position set to {position}")
                else:
                    print(f"Error: Position must be between {self.min_pos} and {self.max_pos}.")
            
            except ValueError:
                print("Invalid input. Please enter an integer.")
