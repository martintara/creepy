# controller.py
from inputs import get_gamepad

class Controller:
    def __init__(self):
        self.A = 0
        self.B = 0
        self.Y = 0

    def update(self):
        events = get_gamepad()
        for event in events:
            if event.code == 'BTN_SOUTH':  # Button A
                self.A = event.state
            elif event.code == 'BTN_EAST':  # Button B
                self.B = event.state
            elif event.code == 'BTN_NORTH':  # Button Y
                self.Y = event.state

    def is_pressed(self, button_name):
        # Check if a specific button is pressed
        if button_name == 'A':
            return self.A == 1
        elif button_name == 'B':
            return self.B == 1
        elif button_name == 'Y':
            return self.Y == 1
        return False
