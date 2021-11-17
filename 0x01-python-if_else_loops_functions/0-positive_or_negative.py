#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if  number > 0 :
    print("{} is: POSITIVE".format(number))
elif number <  0 :
    print(" {} is : NEGATIVE".format(number))
elif  number == 0 :
    print("{} is :ZERO".format(number))

