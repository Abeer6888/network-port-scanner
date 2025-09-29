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
