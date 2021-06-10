#!/usr/bin/env python
# ProjectEuler 0001

m = [x for x in range(1,1000) if x % 3 == 0 or x % 5 == 0 ]
s = sum(m)
#print("{}".format(m))
print("{}".format(s))