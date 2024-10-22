import maestro

# Initialize the servo controller
servo = maestro.Controller()

# Set acceleration for servo channel 0
servo.setRange(15, 200, 10000)
servo.setAccel(15, 25)
servo.setSpeed(15,25)


while True:
    # Ask for user input
    user_input = input("Enter the target position for the servo (or type 'exit' to quit): ")

    if user_input.lower() == 'exit':
        break
    
    # Convert input to integer and set the target position for the servo
    target_position = int(user_input)
    
    # Set the target position for servo 0
    servo.setTarget(15, target_position)
    print(f"Servo target set to {target_position}")

    # Optionally, get and display the current position
    current_position = servo.getPosition(0)
    print(f"Current servo position: {current_position}")

# Close the connection to the servo controller
servo.close()
print("Servo controller closed.")
