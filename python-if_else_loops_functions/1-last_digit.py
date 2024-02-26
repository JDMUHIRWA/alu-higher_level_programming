#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 5:
    print('Last digit of {} is greater than 5'.format(number))
elif number == 0:
    print('Last digit of {} is 0'.format(number))
elif number < 6 and number != 0:
    print('Last digit of {} is less than 6 and not 0'.format(number))
