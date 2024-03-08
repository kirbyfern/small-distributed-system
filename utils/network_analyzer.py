import logging
from scapy.all import IP

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def analyze_packet(packet):
    """
    Analyze a packet and log its details.
    """
    # Check if the packet has an IP layer
    if IP in packet:
        # Extract IP layer information
        ip_layer = packet[IP]

        # Extract common fields
        packet_type = packet.getlayer(0).name
        source_ip = ip_layer.src
        destination_ip = ip_layer.dst
        protocol = ip_layer.proto
        length = len(packet)

        # Note: Scapy's IP layer does not have a 'flags' attribute, so this is removed.
        # If you need to analyze specific protocols (like TCP or ICMP) for flags, you'd access those layers separately.

        # Log the extracted information
        logging.info(f"Type: {packet_type} | Source IP: {source_ip} | Destination IP: {destination_ip} | Protocol: {protocol} | Length: {length}")
    else:
        logging.warning(f"Packet does not contain IP layer: {packet.summary()}")
