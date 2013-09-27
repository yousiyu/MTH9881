'''
Created on Sep 10, 2013

@author: ubuntu
'''

from Library import BSpline
from matplotlib import pyplot
import numpy as np


k = range(-3,17)
knots = [-0.2,-0.13,-0.06,0,0.02,0.06,0.15,0.3,0.8,1.6,3.1,6.1,10.1,15.1,23.1,30.1,35,40,45,50]
ts = np.linspace(0, 23, 30)
ts = ts.tolist()
y0 = []
y1 = []
y2 = []
y3 = []

basis = BSpline.makeSpline(knots)
for i in range(len(ts)): 
	y0.append(basis.b_spline(ts[i], 1, True))
	y1.append(basis.differentiate_b_spline(ts[i], 1))

#y_prime = basis.differentiate_b_spline(27, 3)
#y_int = basis.integrate_b_spline(27, 3)
#for i in range(len(y)): print y_prime[i]

pyplot.figure(1)
pyplot.subplot(411)
pyplot.plot(y0)
pyplot.subplot(412)
pyplot.plot(y1)
pyplot.subplot(413)
pyplot.plot(y2)
pyplot.subplot(414)
pyplot.plot(y3)
pyplot.show()


