#!/usr/bin/env python

import socket

HOST = '192.168.1.31' #'192.168.1.29'  # Standard loopback interface address (localhost)
PORT = 44545  # Port to listen on

print('Listening for client on port ' + str(PORT) + '...')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print('Connected client on ', addr)
data = None
try:
    while data != 'exit':
        data = conn.recv(1024)
        print('>>> ' + data.strip())
finally:
    conn.close()
print('SERVER EXITING...')
print('NOTE: May need to wait for TIME_WAIT to expire before running again')