from pylab import *
from numpy import *

import os


os.chdir("/Users/EmmanuelSchaan/Desktop/script in a script")     # change directory

execfile("subscript1.py")
execfile("subscript2.py")



import sys 
sys.argv=[4,3] # these are the subscript parameters 
execfile("parameterized_subscript.py")


