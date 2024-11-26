## Description
This script demonstrates a **DoS (Denial-of-Service)** attack for **educational purposes only**. It sends UDP packets to a target IP and port to demonstrate the concept of network flooding.

⚠️ **Disclaimer**: Unauthorized use of this tool is illegal and unethical. Use it only in controlled environments with explicit permission.

---

## Why It's a DoS, Not a DDoS
- **DoS**: This script sends all traffic from a single source (your machine), which is a hallmark of DoS attacks.
- **DDoS**: A true Distributed Denial-of-Service attack involves multiple machines sending packets simultaneously, overwhelming the target server.

To create a DDoS-like simulation, you can:
1. Run this script on multiple devices or virtual machines targeting the same server.
2. Use threading or multiprocessing to simulate multiple "sources" from a single machine.
3. Leverage distributed systems like cloud instances to mimic multiple attackers.

---

## Features
- Custom target IP and port input.
- Simulated attack progress display.
- UDP packet flooding for testing server load.

---

## Prerequisites
- Python 3.x installed on your system.

---

## Setup Instructions

### Step 1: Clone the Repository
Clone the repository to your local machine:
```
git clone https://github.com/0xZ1R0/DDos
cd DDos
```

### Step 2: Install Dependencies
No external dependencies are required. Ensure you have Python 3 installed.

---

### Running the script
Run the script to start the DoS simulation:
```
python attack.py
```

When prompted:

- Enter the target IP (e.g., 127.0.0.1 for local testing).
- Enter the target port (e.g., 8080).

---

### Seting up a local server

For testing purposes, you can set up a local HTTP server using Python:

1. Open a terminal and navigate to a directory.
2. Start the server:
```
python -m http.server 8080
```
3. The server will be available at http://127.0.0.1:8080.

---

Original Author: Majid Tdeni
Modified By: 0xZ1R0
