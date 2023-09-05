#!/usr/bin/python3
skip = 2
for i in range(1, 100):
    if i % 10 == 0:
        i += skip
        skip += 1
    if i == 89:
        print("{}".format(i))
        break
    else:
        print("{:02}, ".format(i), end="")
