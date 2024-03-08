import logging
from scapy.all import IP

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def analyze_packet(packet):
    """
    Analyze a packet and log its details.
    """
    if IP in packet:
        packet_type = packet.getlayer(0).name
        time = packet.time
        source_ip = packet[IP].src
        destination_ip = packet[IP].dst
        protocol = packet.proto
        length = len(packet)
        flags = packet.flags if hasattr(packet, 'flags') else None

        logging.info(f"Type: {packet_type} | Time: {time} | Source IP: {source_ip} | Destination IP: {destination_ip} | Protocol: {protocol} | Length: {length} | Flags: {flags}")
    else:
        logging.warning(f"Packet does not contain IP layer: {packet.summary()}")
