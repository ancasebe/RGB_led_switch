import RPi.GPIO as GPIO
import time

# RGB LED pins
red_pin = 17
green_pin = 22
blue_pin = 24

# Rotary encoder pins
clk_pin = 23
dt_pin = 27
sw_pin = 4

# Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# RGB LED
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)

# Pulse width modulation setup
pwm_freq = 1000

red_pwm = GPIO.PWM(red_pin, pwm_freq)
green_pwm = GPIO.PWM(green_pin, pwm_freq)
blue_pwm = GPIO.PWM(blue_pin, pwm_freq)

# Start with LED off
red_pwm.start(0)
green_pwm.start(0)
blue_pwm.start(0)

# Rotary encoder setup
GPIO.setup(clk_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(dt_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(sw_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initial state
color_pwms = [red_pwm, green_pwm, blue_pwm]  # PWM objects for RGB channels
colors = ['Red', 'Green', 'Blue']
color_index = 0  # Starts with Red
brightness_levels = [0, 0, 0]  # Stores brightness for Red, Green, Blue channels
last_rotary_state = GPIO.input(clk_pin)


# Function to update the brightness of the current color and apply all brightness levels
def update_brightness():
    # Update the brightness for the selected color only
    color_pwms[color_index].ChangeDutyCycle(brightness_levels[color_index])
    print(f"Color: {colors[color_index]}, Brightness: {brightness_levels[color_index]}%")

    # Apply all brightness levels to create the mixed color output
    for i, pwm in enumerate(color_pwms):
        pwm.ChangeDutyCycle(brightness_levels[i])  # Apply brightness for each color channel


# Function to switch color when the button is pressed
def switch_color(channel):
    global color_index
    color_index = (color_index + 1) % 3  # Cycle through Red, Green, Blue
    print(f"Switched to {colors[color_index]}")
    update_brightness()  # Set the brightness for the new color


# Function to handle rotary encoder rotation (brightness control)
def adjust_brightness(channel):
    global last_rotary_state
    clk_state = GPIO.input(clk_pin)
    dt_state = GPIO.input(dt_pin)
    
    if clk_state != last_rotary_state:  # Rotary turned
        if dt_state != clk_state:  # Clockwise
            brightness_levels[color_index] = min(brightness_levels[color_index] + 5, 100)  # Increase brightness
        else:  # Counter-clockwise
            brightness_levels[color_index] = max(brightness_levels[color_index] - 5, 0)  # Decrease brightness
        update_brightness()  # Apply the new brightness for all colors
    
    last_rotary_state = clk_state  # Update last rotary state    


# Add event detection for rotary and button
GPIO.add_event_detect(clk_pin, GPIO.BOTH, callback=adjust_brightness)
GPIO.add_event_detect(sw_pin, GPIO.FALLING, callback=switch_color, bouncetime=200)


# Main loop
try:
    print("Rotary encoder ready. Rotate to adjust brightness, press to change color.")
    while True:
        time.sleep(0.1)  # Keep the program running

except KeyboardInterrupt:
    print("Exiting program.")

finally:
    # Cleanup
    red_pwm.stop()
    green_pwm.stop()
    blue_pwm.stop()
    GPIO.cleanup()
