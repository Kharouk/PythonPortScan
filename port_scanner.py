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


# What we want to accomplish:
# python3 port_scanner.py <ip>

