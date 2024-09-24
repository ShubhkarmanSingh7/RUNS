 import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Header

class LidarNode(Node):
    def __init__(self):
        super().__init__('lidar_node')
        self.publisher_ = self.create_publisher(LaserScan, 'scan', 10)
        self.timer = self.create_timer(1.0, self.publish_lidar_data)
        self.get_logger().info("Lidar Node has been started.")

    def publish_lidar_data(self):
        msg = LaserScan()
        msg.header = Header()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = "laser_frame"
        
        # Set LaserScan parameters
        msg.angle_min = -1.57  # -90 degrees in radians
        msg.angle_max = 1.57   # +90 degrees in radians
        msg.angle_increment = 0.01  # radians
        msg.range_min = 0.12   # Minimum range in meters
        msg.range_max = 6.0    # Maximum range in meters
        
        # Populate ranges with dummy data; replace this with actual Lidar data
        num_readings = int((msg.angle_max - msg.angle_min) / msg.angle_increment) + 1
        msg.ranges = [1.0] * num_readings  # Dummy data; replace with actual Lidar data
        
        # Optionally, set time increment and scan time
        msg.time_increment = 0.01  # Adjust based on your Lidar specifications
        msg.scan_time = 1.0         # Adjust based on your scanning frequency
        
        # Optionally initialize intensities if your Lidar supports it
        msg.intensities = [0.0] * num_readings  # Placeholder; replace with actual intensity data if available
        
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
