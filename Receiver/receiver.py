# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 17:14:04 2019

@author: yesh2
"""

import socket                   # Import socket module
#netstat -ano| find portnum #output port status with PID
#taskkill /F /PID <process ID>
port = 63342                    # Reserve a port for your service every new transfer wants a new port or you must wait.
s = socket.socket()             # Create a socket object
host = socket.gethostbyname(socket.gethostname()) #"127.0.0.1"   # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print('Server listening....')

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print('Got connection from ', addr)
    data=conn.recv(1024)
    #conn.send('Thank you')
    # print("data: ", data.decode())
    #conn.close()

    with open('Outfile_name.json', '+a') as f:
        print('file opened')
        # while True:
        print('receiving data...')
        print('type of data: ', type(data))
        # data = conn.recv(1024)
        data=data.decode()
        print('data=', (data))
        if not data:
            break
        # write data to a file
        f.write('\n'+data)
    f.close()


print('Successfully get the file')
#s.close()
#conn.close()
print('connection closed')

# def listen_port():
#
# def receive():