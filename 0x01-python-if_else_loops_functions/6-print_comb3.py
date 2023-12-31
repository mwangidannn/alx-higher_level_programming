#!/usr/bin/python3
# 6-print_comb3.py

"""Print all possible different combinations of two digits in ascending order.

    The two digits must be different - 01 and 10 are considered identical.
    """
for number_1 in range(0, 10):
    for digit2 in range(number_1 + 1, 10):
        if number_1 == 8 and digit2 == 9:
            print("{}{}".format(number_1, digit2))
        else:
            print("{}{}".format(number_1, digit2), end=", ")
