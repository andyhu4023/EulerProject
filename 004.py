'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

from Euler import palindromic
from time import time

start = time()

result = max(i*j for i in range(101, 1000) for j in range(i, 1000) if palindromic(str(i*j)))

print('The answer is %d, it takes %f s.' % (result, time()-start))
