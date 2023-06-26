#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    number = 0
    for count in range(x):
        try:
            print(my_list[count], end="")
            number = number + 1
        except IndexError:
            break
    print()
    return number
