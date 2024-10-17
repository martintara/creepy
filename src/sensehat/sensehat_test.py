from sense_hat import SenseHat
import time

# Initialize the Sense HAT
sense = SenseHat()

# Clear the LED matrix
sense.clear()

# Define some colors
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

# Set a single pixel to red at coordinates (2, 2)
sense.set_pixel(2, 2, red)

# Fill the whole display with blue
sense.clear(blue)

# Wait for a bit
time.sleep(2)

# Create a simple pattern
pattern = [
    red, red, green, green, blue, blue, white, white,
    red, red, green, green, blue, blue, white, white,
    red, red, green, green, blue, blue, white, white,
    red, red, green, green, blue, blue, white, white,
    red, red, green, green, blue, blue, white, white,
    red, red, green, green, blue, blue, white, white,
    red, red, green, green, blue, blue, white, white,
    red, red, green, green, blue, blue, white, white
]

# Display the pattern on the LED matrix
sense.set_pixels(pattern)

# Keep the display on for 5 seconds
time.sleep(5)

# Clear the display
sense.clear()

