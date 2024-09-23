import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class LidarNode(Node):
    def __init__(self):
        super().__init__('lidar_node')
        self.publisher_ = self.create_publisher(LaserScan, 'scan', 10)
        self.timer = self.create_timer(1.0, self.publish_lidar_data)
        self.get_logger().info("Lidar Node has been started.")

    def publish_lidar_data(self):
        msg = LaserScan()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "laser_frame"
        msg.angle_min = -1.57
        msg.angle_max = 1.57
        msg.angle_increment = 0.01
        msg.range_min = 0.12
        msg.range_max = 6.0
        msg.ranges = [1.0] * 360  # Dummy data; replace with actual Lidar data
        
        self.publisher_.publish(msg)
        self.get_logger().info('Published Lidar data.')

def main(args=None):
    rclpy.init(args=args)
    lidar_node = LidarNode()
    rclpy.spin(lidar_node)
    lidar_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
