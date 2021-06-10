#!/usr/bin/env python3
# ProjectEuler 0002

# build fibonacci sequence, might be useful in future problems
f1 = 1
f2 = 2
fib = []
fib.append(f1)
fib.append(f2)
while True:
    temp = f2
    f2 = f2 + f1
    if f2 > 4000000:
        break
    fib.append(f2)
    f1 = temp
print("{}".format(fib))

# filter even
fib = [x for x in fib if x % 2 == 0]
print("{}".format(fib))

s = sum(fib)
print("{}".format(s))