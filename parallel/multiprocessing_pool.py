import multiprocessing
from time import time

def f(i):
   for j in range(int(5.e7)):
      a=0.
   return i


tStart = time()
pool = multiprocessing.Pool(4)

I = range(4)
Result = pool.map(f, I)
print Result

tStop = time()
print tStop-tStart

