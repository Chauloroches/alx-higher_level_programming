#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    a = 0
    try:
        for i in range(x):
            try:
                b = my_list[i]
                if isinstance(b, int):
                    print("{:d}".format(b), end=' ')
                    a += 1
            except IndexError:
                break
        print()  
    except TypeError:
        pass  
    return a
