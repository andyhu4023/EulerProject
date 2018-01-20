'''
Alice plays the following game, she starts with a list of integers LL and on each step she can either:

remove two elements aa and bb from LL and add abab to LL
or conversely remove an element cc from LL that can be written as abab, with aa and bb being two integers such that a,b>1a,b>1, and add both aa and bb to LL
For example starting from the list L={8}L={8}, Alice can remove 88 and add 22 and 33 resulting in L={2,3}L={2,3} in a first step. Then she can obtain L={9}L={9} in a second step.

Note that the same integer is allowed to appear multiple times in the list.

An integer n>1n>1 is said to be creative if for any integer m>1m>1 Alice can obtain a list that contains mm starting from L={n}L={n}.

Find the sum of all creative integers less than or equal to 10121012.
'''

from time import time

start = time()

from math import log10
def creative(a, b, c, bound=10**12):
    result = list()
    step1 = [(a ** b, c), (a ** c, b), (b ** a, c), (b ** c, a), (c ** a, b), (c ** b, a)]
    #result += [i**j, j**i]
    result += [i ** j for i, j in step1 if i<= 10**6 and j<= 10**6 and j*log10(i) <= 12]
    result += [j ** i for i, j in step1 if i<= 10**6 and j<= 10**6 and i*log10(j) <= 12]
    return set(result)

# bound = 10**12* 1.0001
#
# creative_numbers = list()
# #i = 2
# for i in range(2, 10):
#     for j in range(i, int(10**(6/i))+1):
#         temp = creative(2, i, j, bound)
#         print(temp)
#         creative_numbers += temp
# print('-------------')
# for i in range(3, 10):
#     for j in range(i, int(10**(4/i))+1):
#         temp = creative(3, i, j, bound)
#         print(temp)
#         creative_numbers += temp
#
# print(10**12 in creative_numbers)
# result = set(creative_numbers)
# print(len(result))
# print(sum(result) - 16)

from Euler import prim

for i in range(2,10**)

#print('The answer is %d, it takes %f s.' %(result, time()-start))






