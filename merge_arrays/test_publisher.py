#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class TestPublish(Node):

    def __init__(self):
        super().__init__("test_publish_node")
        self.publisher_ = self.create_publisher(String, "/test", 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.publish_message)

    def publish_message(self):
        msg = String()
        msg.data = "Hello World!"
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)

    node = TestPublish()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__ == '__main__':
    main()