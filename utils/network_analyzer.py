from scapy.all import sniff, IP, UDP, TCP
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def packet_callback(packet):
    """
    Callback function to process packets.
    """
    # Ensure the packet has the IP layer
    if IP in packet:
        # Extract packet details
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet.proto
        if proto == 17: # UDP
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
        elif proto == 6: # TCP
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
        else:
            src_port = None
            dst_port = None

        # Calculate length and flags
        length = len(packet)
        flags = None
        if TCP in packet:
            flags = packet[TCP].flags

        # Print packet details
        logging.info(f"Type: {proto} | Time: {packet.time} | Source IP: {src_ip} | Destination IP: {dst_ip} | Source Port: {src_port} | Destination Port: {dst_port} | Protocol: {proto} | Length: {length} bytes | Flags: {flags}")

if __name__ == "__main__":
    # Start sniffing packets
    sniff(prn=packet_callback, filter="udp or tcp", store=0)
