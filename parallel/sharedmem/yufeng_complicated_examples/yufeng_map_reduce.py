import sharedmem
import numpy as np


chunkSize = 10
nChunks = 3
nOps = nChunks * chunkSize

# Input integers, which we would like to sum
input = range(chunkSize * nChunks)


with sharedmem.MapReduce() as pool:
   chunkSize = 10

   def work(i):
       return sum(input[i:i+chunkSize]) # we use the slower python sum operator

   def reduce(r):
       return r

   r = pool.map(work, range(0, nOps, chunkSize))#, reduce=reduce)

print r
print np.sum(r)
