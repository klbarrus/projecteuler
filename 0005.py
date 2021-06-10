#!/usr/bin/env python3
# ProjectEuler 0005

# 20 = 2^2 * 5
# 19
# 18 = 2 * 3^2
# 17
# 16 = 2^4
# 15 = 3 * 5
# 14 = 2 * 7
# 13
# 12 = 2^2 * 3
# 11
# 10 = 2 * 5
#  9 = 3^2
#  8 = 2^3
#  7
#  6 = 2 * 3
#  5
#  4 = 2^2
#  3
#  2
#
# smallest to divide 2-20 is 2^4 * 3^2 * 5 * 7 * 11 * 13 * 17 * 19
smallest = 2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19
print("smallest is {}".format(smallest))