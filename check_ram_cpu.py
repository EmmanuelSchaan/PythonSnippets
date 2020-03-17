import numpy as np
import psutil

'''
# gives a single float value
print psutil.cpu_percent()

# gives an object with many fields
memObject = psutil.virtual_memory()
print memObject

# you can convert that object to a dictionary
memory = dict(psutil.virtual_memory()._asdict())
#memAvail = memory['available']

print memory
'''

#########################################################################

# Get RAM usage of a given process
currentProcess = psutil.Process(pid=None)
print currentProcess.memory_info()

# The quantity of interest is RSS (=resident set size),
# which is the portion of RAM occupied by a process
memory = dict(currentProcess.memory_info()._asdict())
print "RSS:", memory['rss']

# make it a function
def currentRssMB(pid=None):
   """Returns the RSS (resident set size, ie portion of RAM occupied by a process).
   Output in MB.
   """
   memory = dict(psutil.Process(pid=None).memory_info()._asdict())
   return memory['rss'] / 1.e6

#########################################################################

# get the overall CPU usage
print psutil.cpu_percent()


# get the RAM available
memObject = psutil.virtual_memory()
print memObject

memory = dict(psutil.virtual_memory()._asdict())
print "Available RAM:", memory['available']
