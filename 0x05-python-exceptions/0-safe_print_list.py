#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count_num = 0
    for z in range(x):
        try:
            print(my_list[z], end=" ")
            count_num += 1
        except IndexError:
            break

    print("")
    return count_num

