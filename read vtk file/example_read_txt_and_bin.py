from numpy import *
from pylab import *
from scipy import *
from math import *
import struct





#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################

def readvtk(nomfichier):
   #################################### open file #########################

   data = open(nomfichier, 'rb')

   #################################### read header #########################

   data.readline() # ignore 1 line
   line = data.readline()

   t = line.split()[4]
   t = float( t[:len(t)-1] )  # remove the comma at the end of nb

   data.readline()
   data.readline() # ignore 2 lines
   
   line = data.readline()
   [other, Nx, Ny, Nz] = line.split()  # read nb ov vertices
   [Nx, Ny, Nz] = [int(Nx)-1, int(Ny)-1, int(Nz)-1] # get nb of cells

   line = data.readline()
   [other, x0, y0, z0] = line.split()
   [x0, y0, z0] = [float(x0), float(y0), float(z0)]

   line = data.readline()
   [other, dx, dy, dz] = line.split()
   [dx, dy, dz] = [float(dx), float(dy), float(dz)]

   data.readline() # ignore 1 line


#################################### print header #########################

   print '##################################'
   print 't= ', t
   print 'Nx, Ny, Nz = ', Nx, Ny, Nz
   print 'x0, y0, z0 = ', x0, y0, z0
   print 'dx, dy, dz = ', dx, dy, dz
   print '##################################'


#################################### read D #########################

   print 'reading', data.readline()
   data.readline() # ignoring 1 line

   D = zeros((Nx, Ny, Nz))   

   for k in range (Nz):
      for j in range (Ny):
         for i in range (Nx):
            bindata = data.read(4)   # reads the bin for one nb
            D[i,j,k] = struct.unpack('>f', bindata)[0]  # converts into float, from big-endian



#################################### read M1, M2, M3 #########################

   data.readline() # ignore 1 line  
   print 'reading', data.readline()

   M1 = zeros((Nx, Ny, Nz))
   M2 = zeros((Nx, Ny, Nz))
   M3 = zeros((Nx, Ny, Nz))

   for k in range (Nz):
      for j in range (Ny):
         for i in range (Nx):
         
            bindata = data.read(4)              # M1
            M1[i,j,k] = struct.unpack('>f', bindata)[0] 

            bindata = data.read(4)              # M2
            M2[i,j,k] = struct.unpack('>f', bindata)[0] 

            bindata = data.read(4)              # M3
            M3[i,j,k] = struct.unpack('>f', bindata)[0] 


#################################### read B1, B2, B3 #########################

   data.readline() # ignore 1 line
   print 'reading', data.readline()

   B1 = zeros((Nx, Ny, Nz))
   B2 = zeros((Nx, Ny, Nz))
   B3 = zeros((Nx, Ny, Nz))
   
   for k in range (Nz):
      for j in range (Ny):
         for i in range (Nx):
      
            bindata = data.read(4)              # B1
            B1[i,j,k] = struct.unpack('>f', bindata)[0] 

            bindata = data.read(4)              # B2
            B2[i,j,k] = struct.unpack('>f', bindata)[0] 

            bindata = data.read(4)              # B3
            B3[i,j,k] = struct.unpack('>f', bindata)[0] 


#################################### close file #########################

   data.close()
   
   return t, Nx, Ny, Nz, x0, y0, z0, dx, dy, dz, D, M1, M2, M3, B1, B2, B3
   
   
#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################



def slice2d(S, x0, dx, y0, dy):

   Nx = len(S[:, 0])
   Ny = len(S[0, :])

   xi = x0
   xf = x0 + Nx*dx 

   yi = y0
   yf = y0 + Ny*dy

   xx = zeros((Nx+1,Ny+1))               # the dimension has to be one greater than for I, for pcolor
   yy = zeros((Nx+1,Ny+1))
   for i in range (Nx+1):
      yy[i,:] = linspace(yi, yf, Ny+1)
   for j in range (Ny+1):
      xx[:,j] = linspace(xi, xf, Nx+1)

   
   figure(1)
   hold(False)
   pcolor(xx, yy, S)
   #xlabel(r'$x$', fontsize=16)
   #ylabel(r'$y$', fontsize=16)
   hold(True)
   colorbar()
   axis('scaled') 
   #title(r'pcolor', fontsize=20)
   draw()


#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################


def fft_z(S):                 # here no remapping needed because kx=ky=0
   Nx = len(S[:, 0, 0])
   Ny = len(S[0, :, 0])
   Nz = len(S[0, 0, :])
   
   K = linspace(0, Nz-1, Nz)  # array of wave vectors in unit 2*pi/Lz
   
   Sk = zeros(Nz)
   
   for i in range(Nx):
      for j in range(Ny):
         Sk[:] += abs( fft( S[i,j,:] ) ) 
         
   Sk = Sk / (Nx*Ny*Nz)
   return K, Sk  # since S is real, a(k) = a(-k) so we reduce the interval



#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################

def unwrap(S, x0, dx, dy, q, Omega0, t):   # coord change in real space before fft
   Nx = len(S[:, 0, 0])
   Ny = len(S[0, :, 0])
   Nz = len(S[0, 0, :])
   
   newS = zeros((Nx, Ny, Nz))
   
   for i in range(Nx):
      for j in range(Ny):
         
         x = (x0+dx/2) + i * dx   # x coordinate of the center of the current cell
         deltay = -q*Omega0*t * x
         
         Dj = floor( deltay/dy )   # integer nb of j to offset
         dj = deltay/dy - Dj       # remainder of the offset, between 0 and 1
         newj = j + Dj
         newS[i,j,:] = (1-dj) * S[i, newj%Ny, :] + dj * S[i, (newj+1)%Ny, :]  # interpolation, with periodicity

   return newS



def rewrap(S, x0, dx, dy, q, Omega0, t):  # coord change in fourier space after fft, S is the fft
   Nx = len(S[:, 0, 0])
   Ny = len(S[0, :, 0])
   Nz = len(S[0, 0, :])
   
   dkx = 2*pi / ( (Nx-1) * dx )
   dky = 2*pi / ( (Ny-1) * dy )

   newS = zeros((Nx, Ny, Nz))
   
   for i in range(Nx):
      for j in range(Ny):
      
         ky = j * dky         # value of ky corresponding to the current j
         deltakx = -q*Omega0*t * ky    
         
         Di = floor( deltakx/dkx )     # integer nb of 
         di = deltakx/dkx - Di
         newi = i + Di
         newS[i, j, :] = (1-di) * S[inew%Nx, j, :] + di * S[(inew+1)%Nx, j, :]
   
   return newS
   
   

def fft3d(S):   # gives the 3d fft for the unwrapped 3D field
   Nx = len(S[:, 0, 0])
   Ny = len(S[0, :, 0])
   Nz = len(S[0, 0, :]) 
   
   Kx = linspace(0, Nx-1, Nx)
   Ky = linspace(0, Ny-1, Ny)
   Kz = linspace(0, Nz-1, Nz)
   
   newS = abs( fftn(S) ) / (Nx*Ny*Nz)
   
   return Kx, Ky, Kz, newS
   

#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################

nomfichier = 'HGBffttest.0000.vtk'
q = 2.1
Omega0 = 1.e-3



[t, Nx, Ny, Nz, x0, y0, z0, dx, dy, dz, D, M1, M2, M3, B1, B2, B3] = readvtk(nomfichier)






slice2d(M2[:, :, 31], x0, dx, y0, dy)




[Kz, M2kz] = fft_z(M2)

figure(2)
hold(False)
plot(Kz[:Nz/2+1], M2kz[:Nz/2+1])
hold(True)




Kx, Ky, Kz, M2k = fft3d(M2)

figure(3)
hold(False)
plot(Kz, M2k[0, 0, :], 'r')
hold(True)

figure(4)
hold(False)
plot(Kx, M2k[:, 0, 0], 'b')
hold(True)

figure(5)
hold(False)
plot(Ky, M2k[0, :, 0], 'g')
hold(True)















