n = int(input())


def even():
    i = 0
    while True:
        yield i
        i += 2


iterator = even()
for _ in range(n):
    print(iterator.__next__())
# Don't forget to print out the first n numbers one by one here
