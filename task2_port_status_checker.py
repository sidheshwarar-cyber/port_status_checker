# Port Status Checker
import socket

host = input("Enter the system address (e.g., 127.0.0.1): ")
port = int(input("Enter the port number: "))

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(3)
        result = sock.connect_ex((host, port))

    if result == 0:
        print("Port", port, "is OPEN on", host)
    else:
        print("Port", port, "is CLOSED or not reachable on", host)

except socket.gaierror:
    print("Invalid host name or address.")
except ValueError:
    print("Please enter a valid port number.")
except OverflowError:
    print("Port number must be between 0 and 65535.")
