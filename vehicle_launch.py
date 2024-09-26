import rclpy
from rclpy.node import Node
from launch import LaunchDescription
from launch_ros.actions import Node as LaunchNode

def generate_launch_description():
    return LaunchDescription([
        LaunchNode(
            package='autonomous_vehicle',
            executable='camera_node',
            name='camera_node',
            output='screen',
            parameters=[{'param_name': 'param_value'}]  # Add any parameters if needed
        ),
        LaunchNode(
            package='autonomous_vehicle',
            executable='lidar_node',
            name='lidar_node',
            output='screen'
        ),
        LaunchNode(
            package='autonomous_vehicle',
            executable='motor_control_node',
            name='motor_control_node',
            output='screen'
        )
    ])
