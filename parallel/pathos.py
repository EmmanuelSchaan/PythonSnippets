import time
from pathos.multiprocessing import ProcessPool


# instantiate and configure the worker pool
pool = ProcessPool(nodes=3)

print "- Do a blocking (=synchronous) map on the chosen function"
print(pool.map(pow, [1,2,3,4], [5,6,7,8]))

print "- Do a non-blocking (=asynchronous) map, then get the results"
results = pool.amap(pow, [1,2,3,4], [5,6,7,8])
while not results.ready():
    time.sleep(1)
    print(".")
print(results.get())

print "- Do a non-blocking (=asynchronous) map, then extract the results from the iterator"
results = pool.imap(pow, [1,2,3,4], [5,6,7,8])
print("...")
print(list(results))

print "- Do one item at a time, using a pipe"
print(pool.pipe(pow, 1, 5))
print(pool.pipe(pow, 2, 6))

print "- Do one item at a time, using a non-blocking (=asynchronous) pipe"
result1 = pool.apipe(pow, 1, 5)
result2 = pool.apipe(pow, 2, 6)
print(result1.get())
print(result2.get())
