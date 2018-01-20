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
from math import log10
from Euler import prime_under

start = time()

prime = set(prime_under(10**6))
non_prime = set(range(2, 10**6+1)) - prime
prime = {x for x in prime if x <= 1000}

print('Finding primes use %f' %(time() - start))
creative_number = list()
for i in prime:
    creative_number += [i ** j for j in range(4, int(12/log10(i))+1) if j in non_prime]
for i in non_prime:
    creative_number += [i ** j for j in range(2, int(12/log10(i))+1)]

result = sum(set(creative_number)) - 16

print('The answer is %d, it takes %f s.' %(result, time()-start))






