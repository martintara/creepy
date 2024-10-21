import time
import math
from sense_hat import SenseHat

sense = SenseHat()

# Define some colors
blue = [0, 0, 255]
black = [0, 0, 0]

# Function to create a wave pattern
def draw_wave(step):
    # Clear the display
    sense.clear()
    
    # Iterate over the columns (x-axis)
    for x in range(8):
        # Calculate the wave's height using a sine wave function
        # The step is used to animate the wave
        y = int((math.sin(x + step) + 1) * 3.5)  # Shift and scale sine wave to 0-7
        
        # Ensure the result is clamped within the 0-7 range
        y = min(8, max(0, y))
        
        # Set the LED color at the calculated position
        sense.set_pixel(x, y, blue)

# Animate the wave
step = 0
while True:
    draw_wave(step)
    step += 0.2  # Adjust the speed of the wave
    time.sleep(0.1)  # Pause to control the animation speed
