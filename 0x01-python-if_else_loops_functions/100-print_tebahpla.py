#!/usr/bin/python3
def remove_char_at(str, n):
    for i in range(ord('z'), ord('A') - 1, -1):
      print("{:c}".format(i), end="")
