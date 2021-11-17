#!/usr/bin/python3
def uppercase(str):
    for r in str:
        if ord(r) >= ord('a') and ord(r) <= ord('z'):
            char = chr(ord(r) - 32)
        else:
            char = r
        print("{:s}".format(char), end="")
    print('')
