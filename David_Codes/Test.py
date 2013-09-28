'''
Created on Sep 10, 2013

@author: ubuntu
'''

from Library import BSpline
from matplotlib import pyplot
import numpy as np


k = range(-3,17)
knots = [-0.2,-0.13,-0.06,0,0.02,0.06,0.15,0.3,0.8,1.6,3.1,6.1,10.1,15.1,23.1,30.1,35,40,45,50]
ts = [0.00, 0.02, 0.25, 0.27, 0.52, 0.77, 1.02, 1.27, 1.52, 1.77, 2.01, 3.01, 4.01, 5.01, 7.01, 10.01, 12.01, 15.02, 20.02, 25.02, 30.03]
rates = [0.00546, 0.00557, 0.00546, 0.00644, 0.00688, 0.00702, 0.00705, 0.00693, 0.00701, 0.00728, 0.00690, 0.00798, 0.01008, 0.01248, 0.01690, 0.02106, 0.02298, 0.02478,0.02599,0.02660,0.02694]


ts = np.linspace(15.5, 23, 30)
ts = ts.tolist()
y0 = []
y1 = []
		
basis = BSpline.makeBasis(knots)

y = basis.basis(27, 3, True)
y_prime = basis.differentiate(27, 3)
y_integ = basis.integrate_infinity(14, 3, 27)

print y
print y_prime
print y_integ


