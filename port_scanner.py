#! /bin/python3

import socket
import sys
from datetime import datetime

# Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
    # The target is the ip address (the argument we pass in)
    # We translate the hostname to IPv4 in case user doesnt put ip
else:
    print("""
    Invalid amount of arguments, mah dude.
    
    Syntax:
    python3 port_scanner.py <ip>
    ./port_scanner.py <host_name>
    """)
    sys.exit()

print("-" * 50)
print(f"Scanning target: {target}")
print(f"Started at: {datetime.now()}")
print("-" * 50)

try:
    for port in range(21, 90):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1) # wait a sec and if no connection, move on.
        result = s.connect_ex((target, port)) # returns an error indicator, if the port is open result is 0.

        if result == 0:
            print(f"The port {port} is open.")

        s.close()
except KeyboardInterrupt:
    print("\n Exiting the Program.")
    print("See you soon!")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()
except socket.error:
    print("Couldn't connect via socket.")
    sys.exit()
