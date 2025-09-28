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

### Technical Breakdown
the key python networking components used:
| Component                                       |      Explanation  |
|-----------------------------------------------|----------------------------|
|        socket.gethostbyname(host)   | Used to perform DNS resolution, converting a hostname to an IP address before connecting.|
| socket.socket(AF_INET, SOCK_STREAM) |defines a TCP socket for connection-oriented scanning |
|     s.settimeout(0.5)    | 	Crucial for performance. prevents the program from hanging on filtered/closed ports, allowing the scan to proceed quickly|
|  s.connect_ex((ip, port))    |executes a TCP threeway handshake attempt |


## Step by step implementation

Step 1: open your code editor and create a new python file
Step 2: import socket library
step 3: run the code and enter your IP address and the starting port and ending port that need to be scanned



