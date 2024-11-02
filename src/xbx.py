import pygame

# Initialize Pygame
pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("No joystick found!")
else:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Joystick detected: {joystick.get_name()}")

    try:
        while True:
            pygame.event.pump()
            if joystick.get_button(0):  # Button 0 is usually A
                print("Button A pressed")
            if joystick.get_button(1):  # Button 1 is usually B
                print("Button B pressed")
            if joystick.get_button(3):  # Button 3 is usually Y
                print("Button Y pressed")
    except KeyboardInterrupt:
        print("Exited.")

pygame.quit()

