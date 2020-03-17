# Here the goal is to sum the result of each operation on many objects,
# without first storing all the results then summing them.
# This is because we may not have enough memory to store all the results at once.
# This code does partial sums, to allow this.

import sharedmem, numpy as np

nObj = 10000
nProc = 2

# define chunks
nChunk = self.nProc
chunkSize = self.Catalog.nObj / nChunk

# list of indices for each of the nChunk chunks
chunkIndices = [range(iChunk*chunkSize, (i+1)*chunkSize) for iChunk in range(nChunk)]
# make sure not to miss the last few objects:
# add them to the last chunk
chunkIndices[-1] = range((nChunk-1)*chunkSize, nObj)

def stackChunk(iChunk):
   # object indices to be processed
   chunk = chunkIndices[iChunk]
   resMap = 0.
   for iObj in chunk:
      # do whatever operation on each object of the chunk
   return resMap


# dispatch each chunk of objects to a different processor
with sharedmem.MapReduce(np=self.nProc) as pool:
   result = np.array(pool.map(stackChunk, range(nChunk)))

# sum all the chunks
result = np.sum(result, axis=-1)


