#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list is None:
        return None
    else:
        biggest_num = my_list[0]
        for i in range(len(my_list)):
            if i > biggest_num:
                biggest_num = i
        return biggest_num
