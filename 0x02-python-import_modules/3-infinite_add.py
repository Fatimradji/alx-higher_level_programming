#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

f = 0
result = 0
for argument in sys.argv:
    if f != 0:
        result += int(argument)
    else:
        f += 1
print("{:d}".format(result))
