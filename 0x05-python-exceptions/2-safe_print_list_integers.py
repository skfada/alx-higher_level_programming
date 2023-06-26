#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    index = 0
    for count in range(x):
        try:
            print("{:d}".format(my_list[count]), end="")
            index = index + 1
        except(ValueError, TypeError):
            continue
    print()
    return index
