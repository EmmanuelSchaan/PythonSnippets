import numpy as np
import matplotlib.pyplot as plt

# time
Nt = 501
T = np.linspace(0., 10., Nt)

# bits to send
Nbits = 10
Bits = np.array([0, 1, 1, 0, 1, 0, 0, 0, 1, 0])

# time profile of a pulse
def fPulse(t):
   return (t>=0)*(t<1)

# signal sent
Signal = np.sum( Bits[ibit]*fPulse(T - ibit) for ibit in range(Nbits) )

# noise
sigma = 1.5
Noise = np.random.normal(0., sigma, len(T))

# signal + noise
Data = Signal + Noise

# matched filtered data
Filtered = np.array([ np.sum(Data[:]*fPulse(T[:]-T[it])) for it in range(len(T)) ])
Filtered /= np.sum(fPulse(T))

# recovered signal
Recovered = np.sum( (Filtered[ibit*Nt/Nbits] > 0.5)*fPulse(T - ibit) for ibit in range(Nbits) )



fig=plt.figure(0)
ax=plt.subplot(111)
#
ax.plot(T, Signal, 'b', linewidth=3, label=r'signal')
ax.plot(T, Data, 'r', linewidth=1, label=r'signal+noise')
ax.plot(T, Filtered, 'g', linewidth=3, label=r'filtered')
ax.plot(T, Recovered-0.05, 'c', linewidth=3, label=r'recovered')
#
ax.set_ylim((0.-2.*sigma, 0.+2.*sigma))
ax.legend(loc=4)



plt.show()