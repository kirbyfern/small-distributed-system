import socket
import logging

logging.basicConfig(level=logging.INFO)

def broadcast_message(message):
    # Create a UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        #  Enable broadcasting
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        # Broadcast the message
        s.sendto(message.encode(), ('<broadcast>', 12345))
        # Whenever a message being sent
        logging.info("Message sent: %s", message)

if __name__ == "__main__":
    message = "Hello, Nodes!"
    broadcast_message(message)
