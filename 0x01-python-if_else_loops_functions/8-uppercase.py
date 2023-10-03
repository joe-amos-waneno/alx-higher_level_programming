#!/usr/bin/python3
def uppercase(str):
    ans = ''
    for x in str:
        if ord(x) >= 97 and ord(x) <= 122:
            ans += chr(ord(x) - 32)
        else:
            ans += x
    print("{:s}".format(ans))
