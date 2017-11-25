'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

from Euler import factorize
from time import time
start = time()
result = factorize(600851475143)[-1]
print('The answer is %d, it takes %f s.' %(result, time() - start))
