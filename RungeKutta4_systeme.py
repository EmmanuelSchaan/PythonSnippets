#########################################################################################################################
#######################              dX/dt = f(X, t) , with X = (X1, X2, X3, X4)                  #######################
#######################  f can be defined as A*X , giving the coefficients of the matrix A,       #######################
#######################                     or as any function of X and t                         #######################
#########################################################################################################################


from pylab import *
from scipy import linspace


#########################################################################################################################
#########################################################################################################################

############################### PERTURBATION INITIAL VALUES ####################################

X10 = 0. 
X20 = 0.  
X30 = 0.  
X40 = 0. 



###################################### INTEGRATION PARAMETERS ##################################

Ti = 0.
Ti_to_Tf = 10. 

NT = 1001 # number of time points
dT = Ti_to_Tf/(NT-1)  


#########################################################################################################################
#########################################################################################################################


################################### ARRAYS and INITIALIZATION ##################################

T = linspace(Ti, Ti + Ti_to_Tf, NT) # in 1 / Ohm_u units

X1 = zeros(NT) 
X1[0] = X10
X2 = zeros(NT) 
X2[0] = X20
X3 = zeros(NT) 
X3[0] = X30
X4 = zeros(NT) 
X4[0] = X40



############################### LINEAR ODE MATRIX COEFFICIENTS ##############################


def A11(time):
   f = 0.
   return f

def A12(time):
   f = 0.
   return f

def A13(time):
   f = 0.
   return f

def A14(time):
   f = 0.
   return f


def A21(time):
   f = 0.
   return f

def A22(time):
   f = 0.
   return f

def A23(time):
   f = 0.
   return f

def A24(time):
   f = 0.
   return f


def A31(time):
   f = 0.
   return f

def A32(time):
   f = 0.
   return f

def A33(time):
   f = 0.
   return f

def A34(time):
   f = 0.
   return f


def A41(time):
   f = 0.
   return f

def A42(time):
   f = 0.
   return f

def A43(time):
   f = 0.
   return f

def A44(time):
   f = 0.
   return f



##################################### ODE SYSTEM FUNCTIONS #####################################

def f1(x1, x2, x3, x4, time):
   f = A11(time) * x1 + A12(time) * x2 + A13(time) * x3 + A14(time) * x4
   return f

def f2(x1, x2, x3, x4, time):
   f = A21(time) * x1 + A22(time) * x2 + A23(time) * x3 + A24(time) * x4
   return f

def f3(x1, x2, x3, x4, time):
   f = A31(time) * x1 + A32(time) * x2 + A33(time) * x3 + A34(time) * x4
   return f

def f4(x1, x2, x3, x4, time):
   f = A41(time) * x1 + A42(time) * x2 + A43(time) * x3 + A44(time) * x4
   return f


def F(Y, time):
   f = array([ f1(Y[0], Y[1], Y[2], Y[3], time), f2(Y[0], Y[1], Y[2], Y[3], time), f3(Y[0], Y[1], Y[2], Y[3], time), f4(Y[0], Y[1], Y[2], Y[3], time) ])
   return f



########################################### ALGORITHMS ##########################################

def EULER(x1, x2, x3, x4, time, timestep):
   Y = array([ x1, x2, x3, x4 ])
   Y_new = Y + F(Y, time) * timestep
   return Y_new
   
   

def RK4(x1, x2, x3, x4, time, timestep):
   Y = array([ x1, x2, x3, x4 ])
   
   k1 = F(Y, time) * timestep
   k2 = F(Y + k1/2, time + timestep/2) * timestep
   k3 = F(Y + k2/2, time + timestep/2) * timestep
   k4 = F(Y + k3, time + timestep) * timestep

   Y_new = Y + k1/6 + k2/3 + k3/3 + k4/6
   return Y_new
   


########################################### STEPPER ############################################

########################################### MAIN ###############################################

for k in range (NT-1):  # k goes from 0 to NT-2
   X1[k+1], X2[k+1], X3[k+1], X4[k+1] = RK4(X1[k], X2[k], X3[k], X4[k], T[k], dT)



#########################################################################################################################
#########################################################################################################################

####################################### OTHER PHYSICAL QUANTITIES #################################

############################################ VISUALIZATION #####################################

figure(1)
plotlabel= "X1 = f(t)"
hold(False)
plot(T, X1)
hold(True)
title(plotlabel)
draw()

figure(2)
plotlabel= "X2 = f(t)"
hold(False)
plot(T, X2)
hold(True)
title(plotlabel)
draw()

figure(3)
plotlabel= "X3 = f(t)"
hold(False)
plot(T, X3)
hold(True)
title(plotlabel)
draw()

figure(4)
plotlabel= "X4 = f(t)"
hold(False)
plot(T, X4)
hold(True)
title(plotlabel)
draw()


