import numpy as np

##################################################################################
# Path to save the VTK file

pathVtk = "./data.vtk"

##################################################################################
# create fake data, like a galaxy catalog

nObj = 100
# galaxy positions
X = np.random.uniform(low=0., high=1., size=nObj)
Y = np.random.uniform(low=0., high=1., size=nObj)
Z = np.random.uniform(low=0., high=1., size=nObj)
# galaxy velocities
vX = np.random.normal(loc=0., scale=0.1, size=nObj)
vY = np.random.normal(loc=0., scale=0.1, size=nObj)
vZ = np.random.normal(loc=0., scale=0.1, size=nObj)
# scalar property, ie mass
M = np.random.normal(loc=1., scale=0.2, size=nObj)


##################################################################################
# create vtk file

f = open(pathVtk,'w')
f.write('# vtk DataFile Version 3.0\n')
f.write('Catalog data for visualization\n')
f.write('ASCII\n')
f.write('\n')

# Galaxy positions
f.write('DATASET POLYDATA\n')
f.write('POINTS '+str(nObj)+' DOUBLE\n')
for iobj in range(nObj):
   f.write(format(X[iobj], '.10f')+' '+format(Y[iobj], '.10f')+' '+format(Z[iobj], '.10f')+'\n')
f.write('\n')
f.write('POINT_DATA '+str(nObj)+'\n')

# Galaxy velocities
f.write('VECTORS v DOUBLE\n')
for iobj in range(nObj):
   f.write(format(vX[iobj], '.10f')+' '+format(vY[iobj], '.10f')+' '+format(vZ[iobj], '.10f')+'\n')
f.write('\n')

# Galaxy masses
f.write('SCALARS m DOUBLE\n')
f.write('LOOKUP_TABLE default\n')
for iobj in range(nObj):
   f.write(format(M[iobj], '.10e')+'\n')
f.write('\n')

f.close()

