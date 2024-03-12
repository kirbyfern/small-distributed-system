# import socket
# import logging

# logging.basicConfig(level=logging.INFO)

# def broadcast_message(message):
#     # Create a UDP socket
#     with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
#         #  Enable broadcasting
#         s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
#         # Broadcast the message
#         s.sendto(message.encode(), ('<broadcast>', 12345))
#         # Whenever a message being sent
#         logging.info("Message sent: %s", message)

# if __name__ == "__main__":
#     message = "Hello, Nodes!"
#     broadcast_message(message)
#################################
# First master.py draft
#################################

import socket
import logging
import time
from time import sleep

# Configure logging settings to log messages with INFO level
logging.basicConfig(level=logging.INFO)

# Define a function to broadcast a message to all nodes in the network
def broadcast_message(message):
    # Get information about available network interfaces
    interfaces = socket.getaddrinfo(host=socket.gethostname(), port=None, family=socket.AF_INET)
    # Extract IP addresses from the network interfaces information
    allips = [ip[-1][0] for ip in interfaces]

    # Encode the message to bytes
    msg = message.encode()

    # Start time measurement
    start_time = time.time()

    # Continuously send the message to all IP addresses in the network
    while True:
        # Iterate through all IP addresses
        for ip in allips:
            # Print the IP address to which the message is being sent
            print(f'sending a message to {ip}')
            # Create a UDP socket for sending the message
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) as s:
                # Set the socket option to allow broadcasting
                s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
                # Bind the socket to the IP address and a random port
                s.bind((ip, 0))
                # Send the message to the broadcast address on port 12345
                s.sendto(msg, ("<broadcast>", 12345))
        # Introduce a 2-second delay before sending the message again
        sleep(2)

    # End time measurement
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'Execution time: {elapsed_time} seconds')

# Execute the following code if the script is run directly
if __name__ == "__main__":
    # Define the message to be broadcasted
    message = "Hello, Nodes!"
    # Call the function to broadcast the message
    broadcast_message(message)