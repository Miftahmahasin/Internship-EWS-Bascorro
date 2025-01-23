#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool 

class NumberCounter(Node):
    def __init__(self):
        super().__init__('number_counter')
        self.subscription = self.create_subscription(
            Int64,
            'number',
            self.listener_callback,
            10
        )
        self.publishers_ = self.create_publisher(Int64, "number_count", 10)
        self.counter_ = 0
        self.services_ = self.create_service(SetBool, 'reset_number_count', self.reset_counter_callback)
        self.get_logger().info('Service /reset_counter is ready.')
        
    def listener_callback(self, msg):
        self.get_logger().info(f'received {msg.data}')
        self.counter_ += msg.data
        new_msg = Int64()
        new_msg.data = self.counter_
        self.publishers_.publish(new_msg)
        self.get_logger().info(f'number count {new_msg.data}')

    def reset_counter_callback(self, request, response):
        if request.data:
            self.counter_ = 0
            response.success = True
            response.message = "Number count has been reset."
        else:
            response.success = False
            response.message = "Number count reset request ignored."

        self.get_logger().info(response.message)
        return response


def main(args=None):
    rclpy.init(args=args)
    node = NumberCounter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()