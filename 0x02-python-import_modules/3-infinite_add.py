#!/usr/bin/python3

if __name__ == "__main__":
    """outputs  the addition of all para."""
    import sys

    total = 0
    for h in range(len(sys.argv) - 1):
        total += int(sys.argv[h + 1])
    print("{}".format(total))

