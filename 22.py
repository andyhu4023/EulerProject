from time import time

start = time()

file = open('Files/p022_names.txt', 'r').read().strip().split(',')
file = [s.strip('"') for s in file]
file.sort()

result = sum((i+1)*sum(ord(c)-64 for c in file[i]) for i in range(0, len(file)))

print('The answer is %d, it takes %f s.' %(result, time()-start))