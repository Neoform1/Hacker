# write your code here
import socket
import sys
import itertools

args = sys.argv

server_socket = socket.socket()
hostname = args[1]
port = int(args[2])
address = (hostname, port)
server_socket.connect(address)

all_symbols = 'abcdefghijklmnopqrstuvwxyz0123456789'
i = 1
while True:
    for password in itertools.product(all_symbols, repeat=i):
        pw = ''.join(password)
        message = pw.encode()
        server_socket.send(message)
        response = server_socket.recv(1024)
        response = response.decode()
        if response == 'Connection success!':
            print(pw)
            break

    else:
        i += 1
        continue
    break





