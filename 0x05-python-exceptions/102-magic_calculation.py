#!/usr/bin/python3
def magic_calculation(a, b):
    ans = 0
    for q in range(1, 3):
        try:
            if q > a:
                raise Exception('Too far')
            ans += a ** b / q
        except Exception:
            ans = b + a
            break
    return ans
