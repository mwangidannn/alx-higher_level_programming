#!/usr/bin/python3

for f in range(ord('a'), ord('z') + 1):
    if chr(f) != 'e' and chr(f) != 'q':
        print('{:c}'.format(f), end='')
