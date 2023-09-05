#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str_num = str(number)
for digit in str_num:
    last_digit = digit
last_digit = int(last_digit)
if last_digit > 5:
    print(f"Last digit of {number:d} is {last_digit:d} and is greater than 5")
elif last_digit ==  0:
    print(f"Last digit of {number:d} is {last_digit:d} and is 0")
else:
    print(f"Last digit of {number:d} is {last_digit:d} and is less than 6 and not 0")
