N = int(input())  # the initial amount of atoms N
R = int(input())  # the final quantity R

half_life_periods = 0
while N > R:
    N = N / 2
    half_life_periods += 1

print(half_life_periods * 12)
