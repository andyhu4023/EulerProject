'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''

from time import time


def Fibo(n):
    a,b = 0,1
    while b<n:
        a,b = b, a+b
        yield a


start = time()
s = sum(i for i in Fibo(4*10**6) if i%2 ==0)
print('The answer is %d, it takes %f s.' %(s, time()-start))