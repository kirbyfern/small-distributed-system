import socket
import threading
import logging
from network_analyzer import analyze_packet  # Modified import statement

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def receive_messages():
    """
    Start listening for messages and analyze them.
    """
    # Create a UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        try:
            # Bind to all interfaces
            s.bind(('', 12345))
            logging.info("Starting to receive messages...")
            while True:
                # Wait for a message
                data, addr = s.recvfrom(1024)
                packet = IP(data)
                analyze_packet(packet)
                message = data.decode()
                logging.info("Received message: %s from %s", message, addr)
                print(f"Received message: {message} from {addr}")
                # Example task: print the message
                print(f"Task: Processing message {message} from {addr}")
        except Exception as e:
            logging.error("Error receiving message: %s", e)

if __name__ == "__main__":
    # Start the message receiving thread
    threading.Thread(target=receive_messages).start()
