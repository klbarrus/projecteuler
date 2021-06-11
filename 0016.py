#!/usr/bin/env python3
# ProjectEuler 0016

num = str(2**1000)
#num = str(2**15)
digsum = 0
for digits in num:
    digsum += int(digits)

print("digit sum is {}".format(digsum))
