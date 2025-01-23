#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.srv import SetBool

class SetBoolClient(Node):
    def __init__(self):
        super().__init__('number_client')
        self.client = self.create_client(SetBool, 'reset_number_count')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for service to be available...')

    def send_request(self, true):
        request = SetBool.Request()
        request.data = true
        future = self.client.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        return future.result()
    

def main(args=None):
    rclpy.init(args=args)
    node = SetBoolClient()
    response = node.send_request(True)
    node.get_logger().info(f'Response: success={response.success}, message="{response.message}"')
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()