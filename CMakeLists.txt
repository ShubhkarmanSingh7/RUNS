cmake_minimum_required(VERSION 3.5)
project(runs)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)

install(PROGRAMS
  src/motor_control.py
  src/lidar_node.py
  src/camera_node.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
