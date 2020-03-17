# estimates the pulsation of a signal of constant time average,
# by counting the number of times it crosses the average value



from pylab import *
from scipy import linspace


NT = 1000  # number of timesteps
DT = 100.  # total integration time
dT = DT/(NT-1)    # duration of time step

T = linspace(0, DT, NT) 

Y = zeros(NT)
for k in range (NT):
   Y[k] = cos(2*pi*k*dT/5)


figure(1)
hold(False)
plot(T, Y)



def omega(Y, duration):
   N = len(Y)
   counter = 0
   average = 0.

   for k in range (N):
      average = average + Y[k]
   average = average / N

   for k in range (N-1):
      if ( Y[k] < average ) and ( Y[k+1] >= average ):
         counter = counter + 1

   return 2*pi * ( float(counter) / duration )


print(  omega(Y, DT)  )