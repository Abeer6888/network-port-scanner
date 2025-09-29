## Network port scanner ##

## Objective

The Network port scanner project aimed to establish a foundational understanding of network communication and security reconnnaissance by building a simple TCP port scanner in python. The tool demonstrates the principles of the TCP threeway handshake and shows how to identify open ports on a target system, which is a key step in vulnerability assessment.

### Skills Learned


- Development of practical python scripting skills.
- Gaining hands on experience with socket programming to establish network connections.
- Enhanced knowledge of network fundamentals and security vulnerabilities.
- Development of critical thinking and problem-solving skills in cybersecurity.

### Tools Used


- Python's socket library.
- Command Line Interface (CLI)
- Text editor

### The code
This script uses python's built in socket library to scan a range of ports on a specified host.
```python
import socket

def scan(host, ports):
    try:
        ip = socket.gethostbyname(host)
    except socket.gaierror:
        print(f"Host {host} cannot be resolved.")
        return

    # 1. Initialize a flag to track if any open ports are found
    found_open_port = False

    print(f"Starting scan on {host}...")

    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        try:
            s.connect((ip, port))
            print(f"Port {port} is open")
            # 2. Set the flag to True when a port is found
            found_open_port = True
        except socket.error:
            pass
        finally:
            s.close()
    
    # 3. Check the flag after the loop finishes
    if not found_open_port:
        print("No open ports found in the specified range.")


if __name__ == "__main__":
    target = "127.0.0.1"
    ports_list = [21, 22, 80, 443, 8080]
    scan(target, ports_list)
```
### Technical breakdown

the key python networking components used:
| Component                                       |      Explanation  |
|-----------------------------------------------|----------------------------|
|        socket.gethostbyname(host)   | Used to perform DNS resolution, converting a hostname to an IP address before connecting.|
| socket.socket(AF_INET, SOCK_STREAM) |defines a TCP socket for connection-oriented scanning |
|     s.settimeout(0.5)    | 	Crucial for performance. prevents the program from hanging on filtered/closed ports, allowing the scan to proceed quickly|
|  s.connect_ex((ip, port))    |executes a TCP threeway handshake attempt |


## Ports Outcomes
### Technical Breakdown of Port Scan Outcomes

The script performs a TCP Connect Scan for each port. The status is determined by the target's network response:

| Network Event | Code Action | Final Port Status |
| :--- | :--- | :--- |
| **TCP SYN-ACK is received** | `s.connect()` succeeds, the `try` block executes. | **Open** (Printed) |
| **TCP RST is received** | `s.connect()` raises `socket.error`, the `except` block catches it. | **Closed** (Silent) |
| **Connection times out (0.5s)** | `s.connect()` raises `socket.error` (specifically, `socket.timeout`), the `except` block catches it. | **Filtered** (Silent) |

Ref 1: scan outcome

<img width="561" height="92" alt="image" src="https://github.com/user-attachments/assets/1c48ba12-4139-4bf2-934c-f1d2acfa30f3" />

