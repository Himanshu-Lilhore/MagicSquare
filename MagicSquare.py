# Sum these numbers in any pattern (of 4b) to get the same magic number

import random


def getRandom():
    return random.randint(13, 25)


a = getRandom()
b = getRandom()
c = getRandom()
d = getRandom()

print(f"Magic Number : {a+b+c+d}")

print(a, b, c, d)
print(d + 1, c - 1, b - 3, a + 3)
print(b - 2, a + 2, d + 2, c - 2)
print(c + 1, d - 1, a + 1, b - 1)
