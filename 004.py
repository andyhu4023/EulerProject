from Euler import palindromic
from time import time

start = time()

result = max(i*j for i in range(101, 1000) for j in range(i, 1000) if palindromic(str(i*j)))

print('The answer is %d, it takes %f s.' %(result, time()-start))