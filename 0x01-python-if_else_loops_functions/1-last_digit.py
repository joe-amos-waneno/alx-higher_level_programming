#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    con = number * -1
else:
    con = number

ld = con % 10

if number < 0:
    ld = ld * -1

if ld == 0:
    print(f"Last digit of {number:d} is 0 and is 0")
elif ld > 5:
    print(f"Last digit of {number:d} is {ld:d} and is greater than 5")
elif ld < 6:
    print(f"Last digit of {number:d} is {ld:d}\
 and is less than 6 and not 0")
