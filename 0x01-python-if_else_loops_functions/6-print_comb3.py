#!/usr/bin/python3
skip = 1
keep_skipping = 0
for i in range(1, 100):
    if i % 10 == 0:
        skip += 1
        keep_skipping = skip - 1
        continue
    if keep_skipping:
        keep_skipping -= 1
        continue
    if i == 89:
        print("{}".format(i))
        break
    else:
        print("{:02}, ".format(i), end="")
