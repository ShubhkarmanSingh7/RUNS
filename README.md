# Autonomous Vehicle Project

This project implements an autonomous vehicle using ROS 2 Jazzy Jalisco on a Raspberry Pi 5. The vehicle is equipped with TT20 N motors, encoders, LIDAR for obstacle detection, and a camera for visual processing.

runs/
├── launch/
│   └── robot_launch.py
├── src/
│   ├── lidar_node.py
│   ├── motor_control.py
│   └── camera_node.py
├── urdf/
│   └── car.urdf
├── package.xml
└── setup.py
.
- TT20 N motors with encoders.
- RPLIDAR (or similar) for obstacle detection.
- Pi Camera Model 3.

## Installation Steps

1. Clone this repository to your Raspberry Pi:
   ```bash
   git clone https://github.com/your_username/autonomous_vehicle.git
   cd autonomous_vehicle/src/

