### Latest changes:
- **main.py**: The main script that initializes servos and creates a CreepyPod object.
- **creepy_pod.py**: Contains the main `CreepyPod` class responsible for states and movements.
- **leg.py**: Defines the `Leg` class representing each leg.
- **servo.py**: Defines the `Servo` class representing individual servos in each leg.

#### main.py
```python
# main.py hei!
import json
from creepy_pod import CreepyPod
from creepy_state import CreepyState
from maestro import Controller
import maestro
# from leg import Leg
import time

# from servo import Servo

def main():
    def load_leg_params(filename):
        """Load leg parameters from a JSON file."""
        with open(filename, 'r') as file:
            leg_params = json.load(file)
        return leg_params 
    # servo controller communication object
    ctrl = maestro.Controller()
    leg_params = load_leg_params("default_leg_params.json")
    
    creepy_pod = CreepyPod(leg_params, ctrl)  # Initialize CreepyPod in STARTUP state

    # Run state actions until shutdown
    while creepy_pod.state != CreepyState.EXIT:
        creepy_pod.run_state_action()

    print("CreepyPod has shut down.")

if __name__ == "__main__":
    main()
```

#### creepy_pod.py
```python
# creepy_pod.py
import json
from creepy_state import CreepyState
import time
import pygame
from leg import Leg
from maestro import Controller
import display
from gait import Gait
import math

class CreepyPod:
    DEFAULT_CONFIG_FILE = "default_leg_params.json"
    CRAWL_CONFIG_FILE = "crawl_leg_params.json"
    # CONSTRUCTOR
    def __init__(self, leg_params, ctrl : Controller): # NB!!! ctrl : Controller er mini maestro objektet, må ikke forvirres med pygame controller. Bør ryddes opp i!
        # Initialize leg objects
        self.leg_params = []  # Initialize an empty list to store leg parameters
        self.ctrl = ctrl
        self.load_default_config()
        self.initialize_legs()

        self.gait_controller = Gait(self)  # Initialize Gait with CreepyPod reference
        # Initialize Pygame and the controller
        pygame.init()
        pygame.joystick.init()

        if pygame.joystick.get_count() > 0:
            self.controller = pygame.joystick.Joystick(0)
            self.controller.init()
            print(f"Controller detected: {self.controller.get_name()}")
        else:
            print("No controller detected. Exiting.")
            exit()
        self.state = CreepyState.STARTUP # Initial state
        print(f"Entering state: {self.state.name}")

        self.state_actions = {
            CreepyState.DEVMODE: self.devmode_action,
            CreepyState.STARTUP: self.startup_action,
            CreepyState.IDLE: self.idle_action,
            CreepyState.MANUAL: self.manual_action,
            CreepyState.AUTO: self.auto_action,
            CreepyState.SHUTDOWN: self.shutdown_action,
            CreepyState.EXIT: self.exit_action,
            CreepyState.DEVMODE2: self.devmode2_action,
            CreepyState.DEVMODE3: self.devmode3_action
        }

        # Track the previous state of each button to detect single presses
        self.prev_a = 0
        self.prev_b = 0
        self.prev_x = 0
        self.prev_y = 0
        self.prev_left_bumper = 0
        self.prev_right_bumper = 0
        self.start_button_held_start_time = None  # Time when Start button is first pressed

    # FUNCTIONS
    def initialize_legs(self):
        """Initialize legs based on self.leg_params."""
        self.legs = [
            Leg(
                leg_id=i,
                servo_params=leg["servos"],
                ctrl=self.ctrl,
                offset=leg["offset"]
            )
            for i, leg in enumerate(self.leg_params)
        ]
        print("Legs initialized with current parameters")

    def load_default_config(self):
        """Load the default configuration."""
        print("Loading default configuration...")
        self.load_leg_params(self.DEFAULT_CONFIG_FILE)
        self.initialize_legs()

    # Function that loads leg parameters from file
    def load_leg_params(self, filename):
        with open(filename, 'r') as file:
            self.leg_params = json.load(file)

    def load_crawl_config(self):
        """Load the crawl configuration."""
        print("Loading crawl configuration...")
        self.load_leg_params(self.CRAWL_CONFIG_FILE)
        self.initialize_legs()

    def change_state(self, new_state: CreepyState):
        # Only change if the new state is different
        if self.state != new_state:
            print(f"Changing state from {self.state.name} to {new_state.name}")
            self.state = new_state

    def display_state(self):
        print(f"Current state: {self.state.name}")

    def run_state_action(self):
        action = self.state_actions.get(self.state)
        if action:
            action()

    def check_for_state_change(self):
        # Update Pygame event queue
        pygame.event.pump()

        # Read current button states
        a_pressed = self.controller.get_button(0)  # Button A
        b_pressed = self.controller.get_button(1)  # Button B
        x_pressed = self.controller.get_button(2)  # Button X
        y_pressed = self.controller.get_button(3)  # Button Y
        left_bumper_pressed = self.controller.get_button(4)  # Left Bumper
        right_bumper_pressed = self.controller.get_button(5)  # Right Bumper

        # Detect single presses for state changes
        if a_pressed and not self.prev_a:
            self.change_state(CreepyState.MANUAL)
        elif b_pressed and not self.prev_b:
            self.change_state(CreepyState.AUTO)
        elif x_pressed and not self.prev_x:
            self.change_state(CreepyState.DEVMODE2)
        elif y_pressed and not self.prev_y:
            self.change_state(CreepyState.DEVMODE3)

        elif left_bumper_pressed and right_bumper_pressed and not (self.prev_left_bumper and self.prev_right_bumper):
            self.change_state(CreepyState.DEVMODE)

        # Check if Start button is pressed
        start_button_pressed = self.controller.get_button(7)
        if start_button_pressed:
            # If Start button is pressed, start or continue tracking the hold time
            if self.start_button_held_start_time is None:
                self.start_button_held_start_time = time.time()  # Record the time the button was first pressed
            elif time.time() - self.start_button_held_start_time >= 1:
                # If the button has been held for 2 seconds, enter SHUTDOWN state
                self.change_state(CreepyState.SHUTDOWN)
        else:
            # Reset the hold start time if the Start button is released
            self.start_button_held_start_time = None

        # Update previous button states for the next check
        self.prev_a = a_pressed
        self.prev_b = b_pressed
        self.prev_y = y_pressed
        self.prev_left_bumper = left_bumper_pressed
        self.prev_right_bumper = right_bumper_pressed

    def startup_action(self):
        display.startup() # updates sense hat led display
        self.legs[0].initial_position()
        self.legs[1].initial_position()
        self.legs[2].initial_position()
        self.legs[3].initial_position()
        self.legs[4].initial_position()
        self.legs[5].initial_position()
        print("Initializing systems... Please wait.")
        time.sleep(2)  # Simulate delay during startup
        print("System check complete.")
        print("Transitioning to IDLE state.")
        
        # Automatically transition to IDLE state
        self.change_state(CreepyState.IDLE)

    def idle_action(self):
        display.idle()
        print("System is idle.")
        while self.state == CreepyState.IDLE:
            self.check_for_state_change()

    def manual_action(self):
        display.manual()
        print("Tester lower leg på 6 bein")
        self.legs[0].lower_leg()
        self.legs[1].lower_leg()
        self.legs[2].lower_leg()
        self.legs[3].lower_leg()
        self.legs[4].lower_leg()
        self.legs[5].lower_leg()

        while self.state == CreepyState.MANUAL:
            self.check_for_state_change()

    def auto_action(self):
        display.auto() # updating sense hat display
        #testing leg forward+backward
        # self.legs[1].leg_forward()
        # self.legs[4].leg_forward()
        # time.sleep(2)
        # self.legs[1].leg_backward()
        # self.legs[4].leg_backward()
        print("Autonomous mode activated. Navigating environment...")
        while self.state == CreepyState.AUTO:
            self.gait_controller.tripod_gait()
            self.check_for_state_change()

    def shutdown_action(self):
        display.shutdown()
        print("Shutdown procedure started.")
        self.legs[0].initial_position()
        self.legs[1].initial_position()
        self.legs[2].initial_position()
        self.legs[3].initial_position()
        self.legs[4].initial_position()
        self.legs[5].initial_position()
        time.sleep(3)  # Simulate delay during shutdown
        print("Shutdown procedure complete.")
        print("Transitioning to EXIT state.")
        self.change_state(CreepyState.EXIT)
        pygame.quit()  # Properly quit Pygame
        display.disable() # turn off display

    def devmode_action(self): # left+right bumper
        display.devmode()
        self.load_crawl_config()
        print("Developer mode")
        while self.state == CreepyState.DEVMODE:
            self.check_for_state_change()

    def devmode2_action(self): #X
        display.devmode()
        print("Testing IK")
        # Example target coordinates


        # Desired y distance for both legs in the global coordinate system
        y_target_distance = -50  # Move both legs in the negative y direction
        z_target = -100           # Shared z-coordinate for both legs

        # Target coordinates for each leg in the global coordinate system
        x_target_leg1 = 200      # Leg 1 should move along x = 200 in the global system
        x_target_leg2 = 100      # Leg 2 should move along x = 100 in the global system

        # Move leg 1 (center right leg) directly to its target coordinates
        self.legs[1].move_to_coordinates(x_target_leg1, y_target_distance, z_target)

        # Transform target coordinates for leg 2 to match its local offset
        # We need to rotate by -45 degrees since leg 2 has a +45 degree offset
        angle_offset_leg_2 = 45  # Offset of leg 2 in degrees
        x_local_leg2 = x_target_leg2 * math.cos(math.radians(-angle_offset_leg_2)) - y_target_distance * math.sin(math.radians(-angle_offset_leg_2))
        y_local_leg2 = x_target_leg2 * math.sin(math.radians(-angle_offset_leg_2)) + y_target_distance * math.cos(math.radians(-angle_offset_leg_2))

        # Move leg 2 (back right leg) to the transformed local coordinates
        self.legs[2].move_to_coordinates(x_local_leg2, y_local_leg2, z_target)

        time.sleep(1)

        # Desired y distance for both legs in the global coordinate system
        y_target_distance = -100  # Move both legs in the negative y direction
        z_target = -100           # Shared z-coordinate for both legs

        # Target coordinates for each leg in the global coordinate system
        x_target_leg1 = 200      # Leg 1 should move along x = 200 in the global system
        x_target_leg2 = 100      # Leg 2 should move along x = 100 in the global system

        # Move leg 1 (center right leg) directly to its target coordinates
        self.legs[1].move_to_coordinates(x_target_leg1, y_target_distance, z_target)

        # Transform target coordinates for leg 2 to match its local offset
        # We need to rotate by -45 degrees since leg 2 has a +45 degree offset
        angle_offset_leg_2 = 45  # Offset of leg 2 in degrees
        x_local_leg2 = x_target_leg2 * math.cos(math.radians(-angle_offset_leg_2)) - y_target_distance * math.sin(math.radians(-angle_offset_leg_2))
        y_local_leg2 = x_target_leg2 * math.sin(math.radians(-angle_offset_leg_2)) + y_target_distance * math.cos(math.radians(-angle_offset_leg_2))

        # Move leg 2 (back right leg) to the transformed local coordinates
        self.legs[2].move_to_coordinates(x_local_leg2, y_local_leg2, z_target)

        while self.state == CreepyState.DEVMODE2:
            self.check_for_state_change()

    def devmode3_action(self): #y
        display.devmode()
        
        self.legs[1].servos[2].manual_control_angle()
        self.legs[1].servos[1].manual_control_angle()

        while self.state == CreepyState.DEVMODE3:
            self.check_for_state_change()


    def exit_action(self):
        print("Exiting.")
```

#### leg.py
```python
# leg.py
from servo import Servo
from maestro import Controller
import math

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
```

#### servo.py
```python
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
```

