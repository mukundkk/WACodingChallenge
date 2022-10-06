#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32MultiArray

class MergeArrays(Node):

    total_array = []
    array_1_received = False
    array_2_received = False

    def __init__(self):
        # Initialize the node
        super().__init__("old_merge_arrays_node")

        # Create subscribers for the two topics 
        self.array_1_subscriber = self.create_subscription(Int32MultiArray, "/input/array1", 
            self.fetch_array_1_callback, 10)
        self.array_2_subscriber = self.create_subscription(Int32MultiArray, "/input/array2",
            self.fetch_array_2_callback, 10)

        # Create a publisher for the merged array & set the timer to publish the merged array every .33 seconds
        self.array_publisher = self.create_publisher(Int32MultiArray, "/output/array", 10)
        self.timer = self.create_timer(0.33, self.send_merged_array)

    # Append array 1 to the total array
    def fetch_array_1_callback(self, msg):
        # If array 2 has been received, then we've received & appened both arrays so reset the total array
        if self.array_2_received:
            self.total_array = []

        # Append the array 1 data to the total array
        for i in range(len(msg.data)):
            self.total_array.append(msg.data[i])

        # Set a flag to know that we've received array 1
        self.array_1_received = True

    # Append array 2 to the total array
    def fetch_array_2_callback(self, msg):
        # Only append array 2 once array 1 has been received
        if self.array_1_received:
            for i in range(len(msg.data)):
                self.total_array.append(msg.data[i])

        # Set a flag to know that we've received array 2
        self.array_2_received = True

    # Sort the total array
    def sort_array(self):
        self.total_array.sort()
        return self.total_array

    # Publish the sorted, merged array
    def send_merged_array(self):
        # Only publish the merged array once both arrays have been received
        if self.array_1_received and self.array_2_received:
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