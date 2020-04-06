#! /bin/python3

import socket
import sys
from datetime import datetime


def lines():
    print("-" * 20 + "Porto" + "-" * 20)


# Define our target
if len(sys.argv) == 2:
    try:
        target = socket.gethostbyname(sys.argv[1])
        lines()
        print(f"Welcome to Porto. Grab a glass whilst we see what we can get from {target}")
        lines()
    except socket.gaierror:
        lines()
        print("Sorry, that hostname doesn't resolve to any IPv4 Address.")
        lines()
        sys.exit()

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

lines()
print(f"Scanning target: {target}")
print(f"Started at: {datetime.now()}")
lines()

try:
    for port in range(19, 81):
        # Just to note, this is a bad way of doing it, since it goes through each port slowly. This is why we look into
        # something like threading (&)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.2)  # wait a sec and if no connection, move on.
        result = s.connect_ex((target, port))  # returns an error indicator, if the port is open result is 0.

        if result == 0:
            print(f"The port {port} is open.")

        print(f"Trying port {port}.")
        s.close()

except KeyboardInterrupt:
    print("\nExiting the Program.")
    print("See you soon!")
    sys.exit()

except socket.error:
    print("Couldn't connect via socket.")
    sys.exit()
