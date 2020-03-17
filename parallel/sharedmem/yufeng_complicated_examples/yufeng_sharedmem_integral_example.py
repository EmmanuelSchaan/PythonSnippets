"""
    Integrate [0, ... 1.0) with rectangle rule.
    Compare results from
    1. direct sum of 'xdx' (filled by subprocesses)
    2. 'shmsum', cummulated by partial sums on each process
    3. sum of partial sums from each process.

"""
xdx = sharedmem.empty(1024 * 1024 * 128, dtype='f8')
shmsum = sharedmem.empty((), dtype='f8')
shmsum[...] = 0.0

with sharedmem.MapReduce() as pool:

    def work(i):
        s = slice (i, i + chunksize)
        start, end, step = s.indices(len(xdx))
        dx = 1.0 / len(xdx)
        myxdx = numpy.arange(start, end, step) \
                * 1.0 / len(xdx) * dx
        xdx[s] = myxdx
        a = xdx[s].sum(dtype='f8')
        
        with pool.critical:
            shmsum[...] += a

        return i, a

    def reduce(i, a):
        # print('chunk', i, 'done', 'local sum', a)
        return a

    chunksize = 1024 * 1024
    r = pool.map(work, range(0, len(xdx), chunksize), reduce=reduce)

assert_almost_equal(numpy.sum(r, dtype='f8'), shmsum)
assert_almost_equal(numpy.sum(xdx, dtype='f8'), shmsum)
