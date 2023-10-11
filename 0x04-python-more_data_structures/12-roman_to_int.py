#!/usr/bin/python3
def to_subtract(list_num):
    sub = 0
    maximum = max(list_num)

    for t in list_num:
        if maximum > t:
            sub += t

    return (maximum - sub)

def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(rom_n.keys())

    number = 0
    roman = 0
    list_number = [0]

    for q in roman_string:
        for r in list_keys:
            if r == q:
                if rom_num.get(q) <= roman:
                    number += to_subtract(list_number)
                    list_number = [rom_num.get(q)]
                else:
                    list_number.append(rom_num.get(q))

                roman = rom_num.get(q)

    number += to_subtract(list_number)

    return (number)
