# Small Distributed Project Setup Guide
This project is about setting up a distributed system consisting of a master server and four nodes
using Python code and Docker containers. The master server and nodes are configured to
communicate over ports, creating a network named "Proj1-distributed-network" within Docker.
Through this setup, you will gain hands-on experience in deploying and managing distributed
systems in a controlled environment. As shown in the figure, the servers should be managed into
one cluster, and you can manually define one serves as the master server.

Step 1. Build a small distributed system
Step 2: Implement Protocols:

1) Broadcast Protocol Design: Focus on minimizing unnecessary traffic and optimizing message delivery.
2) Unicast Protocol Design: Develop a unicast protocol for one-to-one communication.
3) Multicast Protocol: Develop a multicast protocol that for group communications

Step 3. Monitor the communication

This README will guide you through setting up a small distributed project environment, installing Docker, creating Docker images and containers for the master and node components, and finally, running the `network_analyzer.py` script. It will also provide references to the code for `master.py` and `node.py`.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installing Docker](#installing-docker)
- [Installing python](#installing-python)
- [Creating Docker Images and Containers](#creating-docker-images-and-containers)
- [Network Configuration and Firewall Setup](#network-configuration-and-firewall-setup)
- [Running the Network Analyzer](#running-the-network-analyzer)
- [Code References](#code-references)

## Prerequisites

- An Ubuntu machine with internet access.
- Basic knowledge of Linux command line and Python.
- Docker knowledge and use of docker commands.

## Installing Docker
1. **Update and upgrade your existing list of packages:**
    ```bash
    sudo apt-get update
    ```
    ```bash
    sudo apt-get upgrade && sudo apt-get dist-upgrade
    ```
2. **Install a few prerequisite packages which let `apt` use packages over HTTPS:**
    ```bash
    sudo apt install apt-transport-https ca-certificates curl software-properties-common
    ```
sudo apt install apt-transport-https ca-certificates curl software-properties-common

3. **Add the GPG key for the official Docker repository to your system:**
    ```bash
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    ```
4. **Add the Docker repository to APT sources:**
    ```bash
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
    ```
5. **Update the package database with the Docker packages from the newly added repo:**
    ```bash
    sudo apt-get update
    ```
6. **Make sure you are about to install from the Docker repo instead of the default Ubuntu repo:**
    ```bash
    sudo apt-cache policy docker-ce
    ```
7. **Finally, install Docker:**
    ```bash
    sudo apt install docker-ce
    ```
8. **Docker should now be installed, the daemon started, and the process enabled to start on boot. Check that it's running:**
    ```bash
    sudo systemctl status docker
    ```
## Setting Up Python Environment

1. **Install Python 3 (if not already installed):**

