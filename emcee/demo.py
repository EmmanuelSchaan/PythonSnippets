import numpy as np
import matplotlib.pyplot as plt
import emcee
import triangle

#####################################################################################


def Objective(par, arg1):
   a = par[0]
   b = par[1]
   f =  - (a-1.)**2. / 3.  - (b-3.)**2./4.  + arg1
   return f


ndim = 2 # nb of variables
nwalkers = 250 # nb of points for sampling

# initial guess: array of shape (nwalkers, ndim)
p0 = np.random.rand(ndim * nwalkers).reshape((nwalkers, ndim))

# get sampler instance
sampler = emcee.EnsembleSampler(nwalkers, ndim, Objective, args=[0.])

# let the walker run a bit on their own...
pos, prob, state = sampler.run_mcmc(p0, 100)
sampler.reset()

# do the MCMC sampling
sampler.run_mcmc(pos, 1000)

# check that the process went well: acceptance fraction between 0.25 and 0.5 (?)
print("Mean acceptance fraction: {0:.3f}"
      .format(np.mean(sampler.acceptance_fraction)))

# plot result
for i in range(ndim):
   plt.figure()
   plt.hist(sampler.flatchain[:,i], 100, color="k", histtype="step")
   plt.title("Dimension {0:d}".format(i))


# make a triangle plot
samples = sampler.chain[:, 50:, :].reshape((-1, ndim))
fig = triangle.corner(samples, labels=["$m$", "$b$", "$\ln\,f$"],
                      truths=[1., 3., Objective([1., 3.], 0.)])

plt.show()