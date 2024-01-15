#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
final_digit = abs(number) % 10
if number < 0:
    final_digit = -(final_digit)
astring = "Last digit of {} is {}".format(number, final_digit)
if final_digit > 5:
    print(f"{astring} and is greater than 5")
elif final_digit == 0:
    print(f"{astring} and is 0")
elif final_digit < 6:
    print(f"{astring} and is less than 6 and not 0")
