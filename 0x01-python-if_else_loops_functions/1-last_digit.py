#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_digit = abs(number) % 10
if number < 0:
   num_digit = -num_digit
print("Last digit of {} is {} and is ".format(number, num_digit), end="")
if num_digit > 5:
    print("greater than 5")
elif num_digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
