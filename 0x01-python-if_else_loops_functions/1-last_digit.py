#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
if num >= 0:
    lastdigit = num % 10
elif num < 0:
    lastdigit = (num * -1) % 10 * (-1)

if lastdigit > 5:
    str = "and is greater than 5"
    print("Last digit of {:d} is {:d} {}".format(num, lastdigit, str))
elif lastdigit == 0:
    print("Last digit of {:d} is {:d} and is 0".format(num, lastdigit))
elif lastdigit < 6:
    str = "and is less than 6 and not 0"
    print("Last digit of {:d} is {:d} {}".format(num, lastdigit, str))
