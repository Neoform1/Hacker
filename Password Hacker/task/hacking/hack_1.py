import socket
import sys

args = sys.argv

server_socket = socket.socket()
hostname = args[1]
port = int(args[2])
address = (hostname, port)
server_socket.connect(address)

message = args[3]
message = message.encode()
server_socket.send(message)

response = server_socket.recv(1024)
response = response.decode()
print(response)

server_socket.close()