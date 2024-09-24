import time
from gpiozero import Motor, RotaryEncoder

# Define motor connections (replace GPIO pins with your actual wiring)
motor_a = Motor(forward=17, backward=18)  # Motor A control pins
motor_b = Motor(forward=22, backward=23)  # Motor B control pins

# Define encoder connections (replace GPIO pins with your actual wiring)
encoder_a = RotaryEncoder(24, 25)  # Encoder A pins
encoder_b = RotaryEncoder(26, 27)  # Encoder B pins (if needed)

# Function to move motors forward at a specified speed
def move_forward(speed=1):
    if 0 <= speed <= 1:
        motor_a.forward(speed)
        motor_b.forward(speed)
    else:
        print("Speed must be between 0 and 1.")

# Function to stop motors
def stop_motors():
    motor_a.stop()
    motor_b.stop()

# Main loop
try:
    print("Moving forward...")
    move_forward(0.5)  # Adjust speed as necessary

    while True:
        print(f"Encoder A position: {encoder_a.value}")  # Read encoder A value
        print(f"Encoder B position: {encoder_b.value}")  # Read encoder B value (if used)
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Stopping motors...")
    stop_motors()

finally:
    # Cleanup code (if necessary)
    print("Cleaning up GPIO...")
