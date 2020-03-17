import numpy as np

##################################################################################
# replacing one for loop

# 5 msec
def oneloop1(n=100000):
   result = 0
   for i in range(n+1):
      result += i
   #print result, n*(n+1)/2

# 10 msec
def oneloop2(n=100000):
   result = reduce(lambda x,y: x+y, range(n+1))
   # print result, n*(n+1)/2


##################################################################################
