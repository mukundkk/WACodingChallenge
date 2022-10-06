#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32MultiArray

class MergeArrays(Node):

    total_array = []

    def __init__(self):
        super().__init__("old_merge_arrays_node")
        self.array_1_subscriber = self.create_subscription(Int32MultiArray, "/input/array1", 
            self.fetch_array_1_callback, 10)
        self.array_2_subscriber = self.create_subscription(Int32MultiArray, "/input/array2",
            self.fetch_array_2_callback, 10)
        self.array_publisher = self.create_publisher(Int32MultiArray, "/output/array", 10)
        self.timer = self.create_timer(1, self.send_merged_array)

    def fetch_array_1_callback(self, msg):
        for i in range(len(msg.data)):
            self.total_array.append(msg.data[i])

    def fetch_array_2_callback(self, msg):
        for i in range(len(msg.data)):
            self.total_array.append(msg.data[i])

    def sort_array(self):
        self.total_array.sort()
        return self.total_array

    def send_merged_array(self):
        msg = Int32MultiArray()
        msg.data = self.sort_array()
        self.array_publisher.publish(msg)
        

def main(args=None):
    rclpy.init(args=args)

    node = MergeArrays()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__ == '__main__':
    main()