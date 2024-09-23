cmake_minimum_required(VERSION 3.5)
project(autonomous_vehicle)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(gpiozero REQUIRED)

install(PROGRAMS
  motor_control.py
  lidar_node.py
  camera_node.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
