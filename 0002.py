#!/usr/bin/env python
# ProjectEuler 0002

f1 = 1
f2 = 2
evensum = f2
while True:
    f = f1 + f2
    if f > 4000000:
        break
    if f % 2 == 0:
        evensum += f
    f1 = f2
    f2 = f
print("{}".format(evensum))