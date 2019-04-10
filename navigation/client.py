#!/usr/bin/env python

import socket
import sys

HOST = 'NUC.local'  # 192.168.1.29  # The server's hostname or IP address
PORT = 44545        # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
cmd = None
try:
    while cmd != 'exit':
        print("Enter Command ['forward', 'backward', 'left', 'right' or 'exit']:")
        cmd = sys.stdin.readline().strip()
        s.sendall(cmd)
except:
    s.sendall(b'exit')  # Send exit command on error or keyboard interrupt

print('CLIENT DONE')