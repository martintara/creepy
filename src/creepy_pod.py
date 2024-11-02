# NB move_pod() er fortsatt noe gammelt generert fra chat gpt. se over dette
# har ikke testet dette enda
# creepy_pod.py
from creepy_state import CreepyState
import time
import pygame
#from leg import Leg

class CreepyPod:
    def __init__(self):
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
            CreepyState.SHUTDOWN: self.shutdown_action
        }

        # Track the previous state of each button to detect single presses
        self.prev_a = 0
        self.prev_b = 0
        self.prev_y = 0
        self.prev_left_bumper = 0
        self.prev_right_bumper = 0

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
        elif y_pressed and not self.prev_y:
            self.change_state(CreepyState.SHUTDOWN)
        elif left_bumper_pressed and right_bumper_pressed and not (self.prev_left_bumper and self.prev_right_bumper):
            self.change_state(CreepyState.DEVMODE)

        # Update previous button states for the next check
        self.prev_a = a_pressed
        self.prev_b = b_pressed
        self.prev_y = y_pressed
        self.prev_left_bumper = left_bumper_pressed
        self.prev_right_bumper = right_bumper_pressed

    def startup_action(self):
        print("Initializing systems... Please wait.")
        time.sleep(2)  # Simulate delay during startup
        print("System check complete.")
        print("Transitioning to IDLE state.")
        
        # Automatically transition to IDLE state
        self.change_state(CreepyState.IDLE)

    def idle_action(self):
        print("System is idle. Monitoring sensors...")
        while self.state == CreepyState.IDLE:
            self.check_for_state_change()

    def manual_action(self):
        print("Manual mode activated. Awaiting user input...")
        while self.state == CreepyState.MANUAL:
            self.check_for_state_change()

    def auto_action(self):
        print("Autonomous mode activated. Navigating environment...")
        while self.state == CreepyState.AUTO:
            self.check_for_state_change()

    def shutdown_action(self):
        print("Shutting down systems.")
        pygame.quit()  # Properly quit Pygame

    def devmode_action(self):
        print("Developer mode activated! Performing special operations...")
        while self.state == CreepyState.DEVMODE:
            self.check_for_state_change()
