import itertools

all_symbols = 'abcdefghijklmnopqrstuvwxyz0123456789'
for pw in itertools.product(all_symbols, repeat=3):
    message = ''.join(pw)
    print(pw)