import time
from gpiozero import Motor, RotaryEncoder

# Define motor connections (replace GPIO pins with your actual wiring)
motor_a = Motor(forward=17, backward=18)  # Motor A control pins
motor_b = Motor(forward=22, backward=23)  # Motor B control pins

# Define encoder connections (replace GPIO pins with your actual wiring)
encoder_a = RotaryEncoder(24, 25)  # Encoder A pins

# Function to move motors forward at a specified speed
def move_forward(speed=1):
    motor_a.forward(speed)
    motor_b.forward(speed)

# Function to stop motors
def stop_motors():
    motor_a.stop()
    motor_b.stop()

# Main loop
try:
    print("Moving forward...")
    move_forward(0.5)  # Adjust speed as necessary

    while True:
        print(f"Encoder position: {encoder_a.value}")  # Read encoder value
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Stopping motors...")
    stop_motors()
