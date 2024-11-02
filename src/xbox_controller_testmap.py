import pygame

# Initialize Pygame
pygame.init()
pygame.joystick.init()

# Check if there is at least one joystick connected
if pygame.joystick.get_count() == 0:
    print("No joystick detected. Please connect a joystick.")
    pygame.quit()
    exit()

# Initialize the first joystick
joystick = pygame.joystick.Joystick(0)
joystick.init()
print(f"Joystick detected: {joystick.get_name()}")

def print_button_states():
    # Button mappings
    button_names = {
        0: "A",
        1: "B",
        2: "X",
        3: "Y",
        4: "Left Bumper",
        5: "Right Bumper",
        6: "Back",
        7: "Start",
        8: "Left Stick Press",
        9: "Right Stick Press"
    }

    # Print all button states
    for button_id in range(joystick.get_numbuttons()):
        button_state = joystick.get_button(button_id)
        button_name = button_names.get(button_id, f"Button {button_id}")
        print(f"{button_name}: {'Pressed' if button_state else 'Released'}")

def print_axis_states():
    # Print all axis states (joysticks and triggers)
    for axis_id in range(joystick.get_numaxes()):
        axis_state = joystick.get_axis(axis_id)
        print(f"Axis {axis_id}: {axis_state:.2f}")

def print_dpad_states():
    # Print D-pad states
    hat = joystick.get_hat(0)
    print(f"D-Pad: {hat}")

try:
    print("Press Ctrl+C to exit.")
    while True:
        # Update the event queue
        pygame.event.pump()

        # Print button, axis, and D-pad states
        print_button_states()
        print_axis_states()
        print_dpad_states()

        print("\n" + "-" * 30 + "\n")  # Separate output for readability
        pygame.time.wait(500)  # Wait to avoid spamming the console

except KeyboardInterrupt:
    print("Exiting...")

finally:
    # Clean up Pygame
    pygame.quit()

