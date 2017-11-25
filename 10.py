'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

from time import time

start = time()

result = sum(i for i in range(2, 2*10**6) if all(i % j for j in range(2, int(i**0.5)+1)))

print('The answer is %d, it takes %f s.' % (result, time()-start))
