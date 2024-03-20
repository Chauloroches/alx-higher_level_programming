#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    allfunction = dir()
    for i in range(0, len(allfunction)):
        if allfunction[i][:2] != "_":
            print("{:s}".format(allfunction[i]))
