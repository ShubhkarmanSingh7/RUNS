import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class LidarProcessorNode(Node):
    def __init__(self):
        super().__init__('lidar_processor_node')
        # Subscribe to the `/scan` topic where LiDAR data is published
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.process_scan_data,
            10)
        self.get_logger().info('Lidar Processor Node has been started.')

    def process_scan_data(self, msg):
        # Processing the incoming LiDAR data
        self.get_logger().info(f"Received {len(msg.ranges)} LiDAR scan points.")
        
        # Example: Find the minimum distance from the LiDAR data
        if msg.ranges:
            min_distance = min([r for r in msg.ranges if r > msg.range_min and r < msg.range_max])
            self.get_logger().info(f"Minimum distance detected: {min_distance:.2f} meters")

def main(args=None):
    rclpy.init(args=args)
    lidar_processor_node = LidarProcessorNode()

    try:
        rclpy.spin(lidar_processor_node)  # Spin the node to keep it alive
    except KeyboardInterrupt:
        pass
    finally:
        lidar_processor_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

   
