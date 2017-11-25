'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

from time import time

# Naive implementation
print('Method 1:')
start = time()
s=0
for i in range(1000):
    if i%3 == 0 or i%5 ==0:
        s+= i
print('The answer is %i, it takes %f s.' %(s, time()-start))

# One line code:
print('Method 2')
start = time()
s = sum(i for i in range(1000) if not (i%3 and i%5))
print('The answer is %i, it takes %f s.' %(s, time()-start))

# Analytic Method:
print('Method 3')
start = time()
