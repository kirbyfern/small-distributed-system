import socket
import threading
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def receive_messages():
    # Create a UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        try:
            # Bind to all interfaces
            s.bind(('', 12345))
            logging.info("Starting to receive messages...")
            while True:
                # Wait for a message
                data, addr = s.recvfrom(1024)
                message = data.decode()
                logging.info("Received message: %s from %s", message, addr)
                print(f"Received message: {message} from {addr}")
                # Example task: print the message
                print(f"Task: Processing message {message}")
        except Exception as e:
            logging.error("Error receiving message: %s", e)

def task_processor():
    # Placeholder for other tasks the node can perform
    while True:
        print("Node is performing another task...")
        logging.info("Node is performing another task...")

if __name__ == "__main__":
    # Start the message receiving thread
    threading.Thread(target=receive_messages).start()
    # Start the task processing thread
    threading.Thread(target=task_processor).start()
