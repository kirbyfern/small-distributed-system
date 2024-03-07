from scapy.all import sniff, UDP, IP
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def analyze_packet(packet):
    """
    Analyze a packet and log its details.
    """
    # Ensure the packet is an IP packet and fully decoded
    if IP in packet and UDP in packet:
        # Log packet details
        logging.info(f"Type: UDP | Time: {packet.time} | Source IP: {packet[IP].src} | Destination IP: {packet[IP].dst} | Source Port: {packet[UDP].sport} | Destination Port: {packet[UDP].dport} | Protocol: {packet.proto} | Length: {len(packet)} | Flags: {packet.flags}")
    else:
        logging.warning(f"Packet does not contain IP or UDP layer: {packet.summary()}")

def start_monitoring():
    """
    Start sniffing for UDP packets and analyze them.
    """
    # Sniff for UDP packets and analyze each packet
    sniff(filter="udp", prn=analyze_packet)

if __name__ == "__main__":
    start_monitoring()
