#!/usr/bin/python3
# 100-print_tebahpla.py
q = 0
for i in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(i - q)), end="")
    q = 32 if q == 0 else 0
