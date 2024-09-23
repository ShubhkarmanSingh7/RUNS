import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image

class CameraNode(Node):
    def __init__(self):
        super().__init__('camera_node')
        self.publisher_ = self.create_publisher(Image, 'camera/image', 10)
        self.timer = self.create_timer(1.0, self.publish_camera_image)
        self.get_logger().info("Camera Node has been started.")

    def publish_camera_image(self):
        msg = Image()
        # Fill in image data here; this is just a placeholder.
        
        self.publisher_.publish(msg)
        self.get_logger().info('Published camera image.')

def main(args=None):
    rclpy.init(args=args)
    camera_node = CameraNode()
    rclpy.spin(camera_node)
    camera_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
