# import socket
# import threading
# import logging

# # Configure logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# def receive_messages():
#     """
#     Start listening for messages and log them.
#     """
#     # Create a UDP socket
#     with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
#         try:
#             # Bind to all interfaces
#             s.bind(('', 12345))
#             logging.info("Starting to receive messages...")
#             while True:
#                 # Wait for a message
#                 data, addr = s.recvfrom(1024)
#                 message = data.decode()
#                 logging.info("Received message: %s from %s", message, addr)
#                 print(f"Received message: {message} from {addr}")
#                 # Example task: print the message
#                 print(f"Task: Processing message {message} from {addr}")
#         except Exception as e:
#             logging.error("Error receiving message: %s", e)

# if __name__ == "__main__":
#     # Start the message receiving thread
#     threading.Thread(target=receive_messages).start()
#################################
# First node.py draft
#################################
import socket  # Module for socket operations
import threading  # Module for threading
import logging  # Module for logging
import time

# Configure logging settings
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define function to receive messages
def receive_messages():
    # Create a UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        try:
            # Bind to all interfaces on port 12345
            s.bind(('', 12345))
            # Log message indicating start of message reception
            logging.info("Starting to receive messages...")
            # Continuous loop to receive messages
            while True:
                # Wait for a message
                data, addr = s.recvfrom(1024)
                # Decode received message
                message = data.decode()
                # Log received message
                logging.info("Received message: %s from %s", message, addr)
                # Print received message and sender's address
                print(f"Received message: {message} from {addr}")
                # Prepare response to the received message
                response = f"I received: {message}"
                # Send response back to the sender
                s.sendto(response.encode(), addr)
                # Log the sent response
                logging.info("Sent response: %s to %s", response, addr)
        # Handle exceptions
        except Exception as e:
            # Log error if message reception encounters an error
            logging.error("Error receiving message: %s", e)

# Execute if the script is run directly
if __name__ == "__main__":
    # Start time measurement
    start_time = time.time()

    # Start a new thread for message reception
    threading.Thread(target=receive_messages).start()

    # End time measurement
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'Execution time: {elapsed_time} seconds')
