#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for index in range(list_length):
        try:
            outcome = my_list_1[index] / my_list_2[index]
        except (ValueError, TypeError):
            print("wrong type")
            outcome = 0
        except ZeroDivisionError:
            print("division by 0")
            outcome = 0
        except IndexError:
            print("out of range")
            outcome = 0
        finally:
            new_list.append(outcome)
    return new_list
