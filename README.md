# Distributed Network Systems Project

## Introduction
This project aims to analyze network communications by monitoring and logging details of all communications. The project includes scripts for broadcasting messages, receiving messages, and analyzing network packets. It leverages Docker for containerization, Python for scripting, and Scapy for packet analysis.

## Features
- **Broadcast Messages:** The `master.py` script broadcasts messages to all nodes in the network.
- **Receive Messages:** The `node.py` script listens for messages broadcasted by the master.
- **Network Analysis:** The `network_analyzer.py` script analyzes network packets and logs detailed information about communications.
- **Docker Support:** All scripts can be containerized using Docker, making it easy to deploy and run on any system with Docker installed.

## Prerequisites
- **Docker:** To build and run the project containers.
- **Python:** For script execution.
- **Scapy:** For packet analysis.

## Installation

### Installing Docker
Follow the official Docker documentation to install Docker on your system.
[Docker Installation Guide](https://docs.docker.com/get-docker/)

### Building Docker Images and Containers
1. **Navigate to the Project Directory:** Open a terminal and navigate to the root directory of your project.
2. **Build the Docker Images:**
```
docker build -t master-image .
docker build -t node-image .
```
3. **Run the Containers:**
```
docker run -d --name master master-image
docker run -d --name node1 node-image
docker run -d --name node2 node-image
docker run -d --name node3 node-image
docker run -d --name node4 node-image
```

## Testing
### Testing Master and Node Scripts
1. **Start the Master Container:**
```
docker start master
```
2. **Start the Node Containers:**
```
docker start node1 node2 node3 node4
```
3. **Check Logs:** To verify that messages are being sent and received, check the logs of the master and node containers:
```
docker logs master
docker logs node1
docker logs node2
docker logs node3
docker logs node4
```


### Building and Testing `network_analyzer.py`
1. **Build the `network_analyzer.py` Script:** Ensure that `network_analyzer.py` is in the correct directory as per your project structure.
2. **Run the Script:** Execute the script using Python. You might need to adjust the script to capture packets from the correct interface or network.
```
python3 network_analyzer.py
```

## Configuring Firewall and Enabling Ports
To ensure that your network analysis scripts can communicate effectively, you may need to configure your firewall to allow traffic on specific ports. The exact steps depend on your operating system and firewall software. Generally, you would need to add rules to allow incoming and outgoing traffic on the ports used by your scripts.

## References
- [Scapy Documentation](https://scapy.readthedocs.io/en/latest/)
- [Docker Documentation](https://docs.docker.com/)

##
This project is open-source intended for Networks and Distributed Systems
