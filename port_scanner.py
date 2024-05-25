import socket
import threading

# Function to check a single port
def check_port(ip, port):
    scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scan.settimeout(1)  # Set timeout to 1 second
    try:
        scan.connect((ip, port))
        print(f"Port {port} is open on {ip}")
    except:
        print(f"Port {port} is not open on {ip}")
        # Do nothing if unable to connect
    finally:
        scan.close()

# Function to scan a range of ports
def scan_ports(ip, start, end):
    for port in range(start, end + 1):
        thread = threading.Thread(target=check_port, args=(ip, port))
        thread.start()


# Start scanning
scan_ports('127.0.0.1', 80, 100)
