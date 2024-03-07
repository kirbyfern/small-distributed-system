# import socket
# import logging

# logging.basicConfig(level=logging.INFO)

# def receive_messages():
#     with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
#         s.bind(('', 12345))
#         while True:
#             data, addr = s.recvfrom(1024)
#             message = data.decode()
#             logging.info("node has received message: %s from %s", message, addr)

# if __name__ == "__main__":
#     receive_messages()

import socket
import logging
import argparse

logging.basicConfig(level=logging.INFO)

def receive_messages(node_id, ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((ip, port))
        while True:
            data, addr = s.recvfrom(1024)
            message = data.decode()
            logging.info("Node %s received message: %s from %s", node_id, message, addr)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run a node in the distributed system.')
    parser.add_argument('--node_id', type=str, required=True, help='Unique identifier for the node.')
    parser.add_argument('--ip', type=str, default='127.0.0.1', help='IP address for the node.')
    parser.add_argument('--port', type=int, default=12345, help='Port number for the node.')
    args = parser.parse_args()

    receive_messages(args.node_id, args.ip, args.port)
