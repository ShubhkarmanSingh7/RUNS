import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import Header
import cv2
import numpy as np

class CameraNode(Node):
    def __init__(self):
        super().__init__('camera_node')
        self.publisher_ = self.create_publisher(Image, 'camera/image', 10)
        self.timer = self.create_timer(1.0, self.publish_camera_image)
        self.get_logger().info("Camera Node has been started.")
        
        # Initialize camera
        self.cap = cv2.VideoCapture(0)  # Adjust index if necessary

    def publish_camera_image(self):
        ret, frame = self.cap.read()  # Capture frame from camera
        if not ret:
            self.get_logger().error('Failed to capture image')
            return
        
        # Prepare Image message
        msg = Image()
        msg.header = Header()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.height, msg.width = frame.shape[:2]
        msg.encoding = 'bgr8'  # Change based on your camera output
        msg.data = np.array(frame).tobytes()  # Convert frame to bytes
        
        self.publisher_.publish(msg)
        self.get_logger().info('Published camera image.')

    def destroy_node(self):
        super().destroy_node()
        self.cap.release()  # Release the camera when shutting down

def main(args=None):
    rclpy.init(args=args)
    camera_node = CameraNode()
    rclpy.spin(camera_node)
    camera_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
  
