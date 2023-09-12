#!/usr/bin/env python3
def no_c(my_string):
    new_string = ""
    for i, c in enumerate(my_string):
        if c not in 'cC':
            new_string += my_string[i]
    return new_string
