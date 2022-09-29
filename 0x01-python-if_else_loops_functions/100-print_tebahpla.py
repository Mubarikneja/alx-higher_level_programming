#!/usr/bin/python3
for chara in range(122, 96, -1):
    if (chara % 2 == 0):
        print("{}".format(chr(chara)), end="")
    else:
        print("{}".format(chr(chara - 32)), end="")
