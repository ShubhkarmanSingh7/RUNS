cmake_minimum_required(VERSION 3.5)
project(runs)

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(std_msgs REQUIRED)

# Add executables
add_executable(camera_node src/camera_node.py)
ament_target_dependencies(camera_node rclpy sensor_msgs)

add_executable(lidar_node src/lidar_node.py)
ament_target_dependencies(lidar_node rclpy sensor_msgs)

add_executable(motor_control src/motor_control.py)
ament_target_dependencies(motor_control_node rclpy std_msgs)

# Install executables
install(TARGETS
  camera_node
  lidar_node
  motor_control
  DESTINATION lib/${PROJECT_NAME})

# Install launch files
install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME})

ament_package()
