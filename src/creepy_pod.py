# creepy_pod.py
from creepy_state import CreepyState
import time
import pygame
from leg import Leg
from maestro import Controller
import display
class CreepyPod:
    def __init__(self, leg_params, controller : Controller):
        # Initialize leg objects
        self.legs = [
            Leg(
                leg_id=i,
                servo_params=leg["servos"],  # Pass only the servos list
                controller=controller,
                offset=leg["offset"]  # Pass the orientation offset for the leg
            )
            for i, leg in enumerate(leg_params)
        ]
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
            CreepyState.EXIT: self.exit_action
        }

        # Track the previous state of each button to detect single presses
        self.prev_a = 0
        self.prev_b = 0
        self.prev_y = 0
        self.prev_left_bumper = 0
        self.prev_right_bumper = 0
        self.start_button_held_start_time = None  # Time when Start button is first pressed

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
        y_pressed = self.controller.get_button(3)  # Button Y
        left_bumper_pressed = self.controller.get_button(4)  # Left Bumper
        right_bumper_pressed = self.controller.get_button(5)  # Right Bumper

        # Detect single presses for state changes
        if a_pressed and not self.prev_a:
            self.change_state(CreepyState.MANUAL)
        elif b_pressed and not self.prev_b:
            self.change_state(CreepyState.AUTO)
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
        print("Initializing systems... Please wait.")
        time.sleep(2)  # Simulate delay during startup
        print("System check complete.")
        print("Transitioning to IDLE state.")
        
        # Automatically transition to IDLE state
        self.change_state(CreepyState.IDLE)

    def idle_action(self):
        display.idle()
        print("System is idle. Monitoring sensors...")
        while self.state == CreepyState.IDLE:
            self.check_for_state_change()

    def manual_action(self):
        display.manual()
        print("Manual mode activated. Awaiting user input...")
        self.legs[0].lower_leg()
        self.legs[1].lower_leg()
        self.legs[2].lower_leg()
        self.legs[3].lower_leg()
        self.legs[4].lower_leg()
        self.legs[5].lower_leg()

        while self.state == CreepyState.MANUAL:
            self.check_for_state_change()

    def auto_action(self):
        display.auto() # updating display
        #testing leg forward+backward
        self.leg[1].leg_forward()
        time.sleep(2)
        self.leg[4].leg_forward()
        print("Autonomous mode activated. Navigating environment...")
        while self.state == CreepyState.AUTO:
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

    def devmode_action(self):
        display.devmode()
        print("Developer mode activated! Performing special operations...")
        while self.state == CreepyState.DEVMODE:
            self.check_for_state_change()

    def exit_action(self):
        print("Exiting.")