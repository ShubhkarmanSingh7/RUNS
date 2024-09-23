# Autonomous Vehicle Project

This project implements an autonomous vehicle using ROS 2 Jazzy Jalisco on a Raspberry Pi 5. The vehicle is equipped with TT20 N motors, encoders, LIDAR for obstacle detection, and a camera for visual processing.

## Project Structure
autonomous_vehicle/
├── autonomous_vehicle/
│ ├── motor_control.py # Controls the motors and reads encoder values.
│ ├── lidar_node.py # Handles LIDAR data publishing.
│ ├── camera_node.py # Captures images from the camera.
│ ├── init.py # Package initialization.
│ ├── CMakeLists.txt # Build configuration for ROS.
│ ├── package.xml # Package metadata and dependencies.
│ └── setup.py # Python package setup.
└── README.md # Project overview and instructions.

## Requirements

- Raspberry Pi 5 with ROS 2 Jazzy Jalisco installed.
- TT20 N motors with encoders.
- RPLIDAR (or similar) for obstacle detection.
- Pi Camera Model 3.

## Installation Steps

1. Clone this repository to your Raspberry Pi:
   ```bash
   git clone https://github.com/your_username/autonomous_vehicle.git
   cd autonomous_vehicle/src/

