import numpy as np
import pylab
Polynomial = np.polynomial.Polynomial

y = np.array([108.7,110.4,112.5,116.1,116.6,117.1,119.0])
x = np.array([36.1,42.0,45.2,50,55,60,65])
cmin, cmax = min(x), max(x)
pfit, stats = Polynomial.fit(x, y, 1, full=True, window=(cmin, cmax),domain=(cmin, cmax))
pylab.plot(x, y, 'o', color='k')
pylab.plot(x, pfit(x), color='k')
pylab.xlabel("Temperature in C")
pylab.ylabel("Resistance in ohm")
pylab.title("RTD temp vs resis")
pylab.grid()
pylab.show()
