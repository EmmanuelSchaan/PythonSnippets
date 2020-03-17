# This takes a function "functionToBeCached",
# and makes it such that the output can be cahed, and referred to with a cache name string.
# If no cache name string is provided, the output is just recomputed.

###########################################################################

class TestClass(object):
   
      def __init__(self):
         pass

      def functionToBeCached(self, cache=None):
         
         # actual calculation to do
         def doCalculation():
            print "doing the calculation"
            result = 0.
            return result
         
         
         # if no caching is desired, just compute
         if cache is None:
            print "don't want to cache"
            result = doCalculation()
         
         # if caching is desired
         else:
            # if first call with caching
            if not hasattr(self.functionToBeCached.__func__, "cache"):
               self.functionToBeCached.__func__.cache = {}
         
            print self.functionToBeCached.__func__.cache, cache
         
            # if the calculation has been done before
            if self.functionToBeCached.cache.has_key(cache):
               print "caching; same as previous calculation"
               result = self.functionToBeCached.cache[cache]
            
            # if this calculation was not done before
            else:
               print "caching; first time for this calculation"
               result = doCalculation()
               self.functionToBeCached.cache[cache] = result
         
         return result


###########################################################################

testClass = TestClass()


print testClass.functionToBeCached()
print testClass.functionToBeCached(cache="bla")
print testClass.functionToBeCached(cache="bla")
print testClass.functionToBeCached(cache="bli")
print testClass.functionToBeCached(cache="bli")
print testClass.functionToBeCached(cache="bla")
print testClass.functionToBeCached()
