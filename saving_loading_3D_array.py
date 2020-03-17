import numpy as np


def write(filename, data):

   with file(filename, 'w') as outfile:
      # I'm writing a header here just for the sake of readability
      # Any line starting with "#" will be ignored by numpy.loadtxt
      outfile.write('# Array shape: {0}\n'.format(data.shape))

      # Iterating through a ndimensional array produces slices along
      # the last axis. This is equivalent to data[i,:,:] in this case
      for data_slice in data:

         # The formatting string indicates that I'm writing out
         # the values in left-justified columns 7 characters in width
         # with 2 decimal places.  
         np.savetxt(outfile, data_slice)

         # Writing out a break to indicate different slices...
         outfile.write('# New slice\n')





# Generate some test array
my_array = np.arange(200).reshape((4,5,10))
print(my_array)

# Write the array to disk
write('array_file.txt', my_array)

# Recover the array from the file
new_array = np.loadtxt('array_file.txt').reshape((4,5,10))
print(my_array - new_array)