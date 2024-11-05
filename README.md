# RGB LED Color Mixer with Rotary Encoder

This project allows you to control the brightness and color of an RGB LED connected to a Raspberry Pi using a rotary encoder. You can adjust the brightness of each color channel (Red, Green, Blue) individually, and the RGB LED will display the combined color based on the current settings. Pressing the button on the rotary encoder will switch between colors (Red, Green, Blue) for individual brightness adjustment.

![Circuit Diagram](circuit_image.jpg) <!-- Link or upload the image of your circuit here -->

## Features
- Adjust individual brightness levels of Red, Green, and Blue channels using a rotary encoder.
- Mix colors by setting different brightness levels for each color, allowing for a full spectrum of colors.
- Simple button press to switch between color channels.

## Hardware Components
- Raspberry Pi 4 with coding environment
- RGB LED (4-legged)
- Rotary Encoder 
- Resistors
- Breadboard and cables

## Circuit Diagram
Refer to the image above to see the complete wiring diagram. The RGB LED and rotary encoder are connected to the Raspberry Pi's GPIO pins.

### Wiring Guide
- **RGB LED Connections**:
  - Red LED pin: GPIO 17
  - Green LED pin: GPIO 22
  - Blue LED pin: GPIO 24
  - Common cathode (or anode) to GND (use resistors for each LED pin).
  
- **Rotary Encoder Connections**:
  - **Clock (CLK) pin**: GPIO 23
  - **Data (DT) pin**: GPIO 27
  - **Switch (SW) pin**: GPIO 4
  - Common ground pin to GND on Raspberry Pi.

### Prerequisites
To run this script, you need the following Python library:
- `rpi-lgpio` - The GPIO library for Raspberry Pi.

You can install the library by running:
```bash
pip install -r requirements.txt
