from pylab import *
import pickle


# define a function
def f(x,y,z):
   return 2.*x + 3.*y + 4.*z

filename = "./function_f.txt"


# create a file and dump the function in it
file = open(filename, 'wb')
pickle.dump(f, file)
file.close()


# open the file and get the function back from it
file = open(filename, 'rb')
newf = pickle.load(file)
file.close()


# check that both functions are the same
print("f(1, 2, 3) = " + str(f(1., 2., 3.)))
print("newf(1, 2, 3) = " + str(newf(1., 2., 3.)))