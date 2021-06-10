#!/usr/bin/env python3
# ProjectEuler 0006

# sum of squares = n(n+1)(2n+1)/6
# https://en.wikipedia.org/wiki/Square_pyramidal_number
#
# square of sums = ( n(n+1)/2 )^2
# https://en.wikipedia.org/wiki/Triangular_number

N = 100
sum_sq = N * (N + 1) * (2*N + 1) / 6
sq_sum = (N * (N + 1) / 2)**2

print("difference is {}".format(sq_sum - sum_sq))