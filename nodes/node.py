# import socket
# import logging
# import argparse

# logging.basicConfig(level=logging.INFO)

# def receive_messages(node_id, port):
#     with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
#         s.bind(('', port))
#         while True:
#             data, addr = s.recvfrom(1024)
#             message = data.decode()
#             logging.info("Node %s received message: %s from %s", node_id, message, addr)

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description='Run a node in the distributed system.')
#     parser.add_argument('--node_id', type=str, required=True, help='Unique identifier for the node.')
#     parser.add_argument('--port', type=int, default=12345, help='Port number for the node.')
#     args = parser.parse_args()

#     receive_messages(args.node_id, args.port)


import socket
import threading

def receive_messages():
    # Create a UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        # Bind to all interfaces
        s.bind(('', 12345))
        while True:
            # Wait for a message
            data, addr = s.recvfrom(1024)
            print(f"Received message: {data.decode()} from {addr}")
            # Example task: print the message
            print(f"Task: Processing message {data.decode()}")

def task_processor():
    # Placeholder for other tasks the node can perform
    while True:
        print("Node is performing another task...")

if __name__ == "__main__":
    # Start the message receiving thread
    threading.Thread(target=receive_messages).start()
    # Start the task processing thread
    threading.Thread(target=task_processor).start()
