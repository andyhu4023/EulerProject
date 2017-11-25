'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
'''

from time import time
from math import factorial

start = time()

result = factorial(40)/factorial(20)**2

print('The answer is %d, it takes %f s.' %(result, time()-start))