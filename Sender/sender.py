# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 17:14:17 2019

@author: yesh2
"""

import socket                   # Import socket module

s = socket.socket()             # Create a socket object
host = socket.gethostbyname(socket.gethostname()) #10.6.34.166"  #Ip address that the TCPServer  is there
port = 63342                     # Reserve a port for your service every new transfer wants a new port or you must wait.

# s.connect((host, port))
# s.send("Hello".encode())

# filename='File2send\\sensor.json' #In the same folder or path is this file running must the file you want to tranfser to be
# f = open(filename,'r')
# l = f.read(1024)
# while(l):
#     s.send(l.encode())
#     print('Sent ',repr(l.encode()))
#     l = f.read(1024)
#     f.close()

# print('Done sending')
# s.send('Thank you for connecting'.encode())
# s.close()

def check_connect():
    # s = socket.socket()  # Create a socket object
    # host = socket.gethostbyname(socket.gethostname())  # 10.6.34.166"  #Ip address that the TCPServer  is there
    # port = 63342  # Reserve a port for your service every new transfer wants a new port or you must wait.
    s.connect((host, port))
    print("Connected")
    # s.send("Hello".encode())

def send(data):
    check_connect()
    s.send(data.encode())
    print('Sent ', repr(data.encode()))
    # l = f.read(1024)
    # f.close()
    # s.send('Thank you for connecting'.encode())
    s.close()

# send({'Message': 'Hi I am Basit'})