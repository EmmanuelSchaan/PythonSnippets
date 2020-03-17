import sharedmem
import numpy as np
import time

# number of processes to use
nProc = 4

# number of times the operation has to be executed
nOps = 100
# Input values to evaluate the operation on
IOp = range(nOps)

# operation to be executed many times
def operation(i):
   time.sleep(0.01)   # number of sec to sleep, to simulate the duration of one operation
   return i


######################################################################
# Most basic pool.map

# Serial version: takes 1 sec
tStart = time.time()
result = map(operation, IOp)
tStop = time.time()
print "Serial version took", tStop-tStart, "sec"
#print "result =", result


# Parallel version: takes 0.25 sec on my quad core laptop
tStart = time.time()
with sharedmem.MapReduce(np=nProc) as pool:
   result = pool.map(operation, IOp)
tStop = time.time()
print "Parallel version took", tStop-tStart, "sec"
#print "result =", result


######################################################################
# Breaking it into chunks explicitly seems to speed up sharedmem

chunkSize = 10
nChunk = int(nOps // chunkSize)

def chunk(iChunk):
   result = map(operation, IOp[iChunk*chunkSize:(iChunk+1)*chunkSize])
   return result

def reduce(result):
   return result

# Serial version
tStart = time.time()
result = map(chunk, range(nChunk))
tStop = time.time()
print "Serial version took", tStop-tStart, "sec"
#print "result =", result


# Parallel version
tStart = time.time()
with sharedmem.MapReduce(np=nProc) as pool:
   result = pool.map(chunk, range(nChunk), reduce=reduce)
tStop = time.time()
print "Parallel version took", tStop-tStart, "sec"
#print "result =", result

