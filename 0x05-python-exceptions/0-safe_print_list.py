#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count_num = 0
    try:
        for z in range(x):
            print(my_list[z], end=" ")
            count_num += 1
    except IndexError:
        pass

    print()  # Print a new line
    return count_num
