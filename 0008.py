#!/usr/bin/env python
# ProjectEuler 0008, Largest product in a series

with open('./0008.txt') as f:
    num = f.read().replace('\n','')
f.close()

maxmul = 0
for i in range(0,len(num)-13):
    digits = num[i:i+13]
    if '0' in digits:
        continue
    arr = [int(x) for x in digits]
    print("{}".format(arr))
    mul = 1
    for j in arr:
        mul *= j
    if mul > maxmul:
        maxmul = mul
print("{}".format(maxmul))