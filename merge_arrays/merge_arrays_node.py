#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

import message_filters

from std_msgs.msg import Int32MultiArray

class MergeArrays(Node):

    total_array = []

    def __init__(self):
        super().__init__("merge_arrays_node")
        self.array_1_subscriber = message_filters.Subscriber('/input/array1', Int32MultiArray)
        self.array_2_subscriber = message_filters.Subscriber('/input/array2', Int32MultiArray)

        ts = message_filters.ApproximateTimeSynchronizer([self.array_1_subscriber, self.array_2_subscriber], 
            10, 0.1, allow_headerless=True)
        ts.registerCallback(self.callback)

    def callback(self):
        self.total_array = self.array_1_subscriber.get_last_message().data + self.array_2_subscriber.get_last_message().data
        self.total_array.sort()

        msg = Int32MultiArray()
        msg.data = self.total_array
        array_publisher = self.create_publisher(Int32MultiArray, "/output/array", 10)
        array_publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)

    node = MergeArrays()
    rclpy.spin(node)

    rclpy.shutdown()

if __name__ == '__main__':
    main()