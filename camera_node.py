import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import Header
import cv2
from cv_bridge import CvBridge  # For image encoding

class CameraNode(Node):
    def __init__(self):
        super().__init__('camera_node')
        self.publisher_ = self.create_publisher(Image, 'camera/image', 10)
        self.timer = self.create_timer(0.033, self.publish_camera_image)  # ~30 FPS
        self.bridge = CvBridge()  # Initialize cv_bridge for encoding conversion

        # Initialize camera
        self.cap = cv2.VideoCapture(0)  # Adjust the index if necessary
        if not self.cap.isOpened():
            self.get_logger().error('Failed to open camera')
            raise RuntimeError('Camera could not be initialized')

        self.get_logger().info("Camera Node has been started.")

    def publish_camera_image(self):
        ret, frame = self.cap.read()  # Capture frame from camera
        if not ret:
            self.get_logger().error('Failed to capture image')
            return

        # Convert OpenCV image to ROS2 Image message
        msg = self.bridge.cv2_to_imgmsg(frame, encoding="bgr8")
        msg.header = Header()
        msg.header.stamp = self.get_clock().now().to_msg()

        self.publisher_.publish(msg)
        self.get_logger().debug('Published camera image.')

    def destroy_node(self):
        super().destroy_node()
        self.cap.release()  # Release the camera when shutting down
        self.get_logger().info("Camera Node has been shut down and camera released.")

def main(args=None):
    rclpy.init(args=args)
    camera_node = CameraNode()
    
    try:
        rclpy.spin(camera_node)
    except KeyboardInterrupt:
        pass
    finally:
        camera_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
