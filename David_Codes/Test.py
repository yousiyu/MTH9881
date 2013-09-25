'''
Created on Sep 10, 2013

@author: ubuntu
'''

from Library import BSpline
#from matplotlib import pyplot



k = range(-3,17)
knots = [-0.2,-0.13,-0.06,0,0.02,0.06,0.15,0.3,0.8,1.6,3.1,6.1,10.1,15.1,23.1,30.1,35,40,45,50]

basis = BSpline.makeSpline(knots)
y = basis.b_spline(27, 3)
y_prime = basis.differentiate_b_spline(27, 3)
y_int = basis.integrate_b_spline(27, 3)



#for i in range(len(y)): print y_prime[i]

print y
print y_prime
print y_int