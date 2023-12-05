#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    multiples_divi = []
    for k in range(len(my_list)):
        if my_list[k] % 2 == 0:
            multiples_divi.append(True)
        else:
            multiples_divi.append(False)

    return (multiples_divi)
