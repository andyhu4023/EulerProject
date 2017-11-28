'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

from Euler import prime_under
from time import time

start = time()

result = prime_under(10**6)[10**4]

print('The answer is %d, it takes %f s.' %(result, time()-start))