#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    names = dir()
    for f in range(0, len(names)):
        if names[f][0:2] != "__":
            print("{}".format(names[f]))
