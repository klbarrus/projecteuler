#!/usr/bin/env python3
# ProjectEuler 0008, Largest product in a series

import math

with open('./0008.txt') as f:
    num = f.read().replace('\n','')
f.close()
#print("{}".format(num))

many = 13
maxmul = 0
maxind = 0
for i in range(0,len(num)-many+1):
    digits = num[i:i+many]
    if '0' in digits:
        continue
    arr = [int(x) for x in digits]
    mul = math.prod(arr)
    #print("{} : {}".format(arr, mul))
    if mul > maxmul:
        maxmul = mul
        maxind = i
print("max product {} at index {}".format(maxmul, maxind))