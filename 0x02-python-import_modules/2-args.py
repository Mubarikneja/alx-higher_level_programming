#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    sys.argv.pop(0)
    arg_len = len(sys.argv)

    if (arg_len == 0):
        print("0 arguments.")
    elif (arg_len == 1):
        print("1 argument:")
        print("{:d}: {}".format(len(sys.argv), sys.argv[0]))
    else:
        print("{:d} arguments:".format(arg_len))
        number = 1
        for argument in sys.argv:
                print("{:d}: {}".format(number, argument))
                number += 1
