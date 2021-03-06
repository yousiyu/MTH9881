'''
Created on Sep 22, 2013

@author: David Herssein
'''

import numpy as np

class SplineBasis(object):
    '''
    This is a simple B-Spline class. For a given set of knot points, 
    these objects are able to calculate the B-spline, its derivative, 
    and its integral about a given point.
    '''

    def __init__(self, knots):
        '''
        Constructor
        knots = vector of knot points
        '''
        self.knots = knots

    def basis(self, x, dim, scalar = True):
		'''
		x is the value at which to evaluate the spline
		d is the order of the b-spline
		scalar is a boolean to decide whether to return the values for all the B-splines 
			or just the k-th one.
		'''
		y = self.knots

		d = dim+1
		N = len(y)
		result = np.zeros((N,d))

		# find the knot points that x lies between
		for i in xrange(N-1):
			if(x>y[i] and x<=y[i+1]): 
				result[i][0] = 1
				place = i

		#iterate over the relevant splines    
		for i in xrange(1,d):
			for j in xrange(place-i-1, place+1):
				result[j][i] = ((x - y[j])/(y[j+i] - y[j]))*result[j][i-1] + ((y[j+i+1]-x)/(y[j+i+1] - y[j+1]))*result[j+1][i-1]

		if(scalar): 
			return result[place,dim]
		else: 
			return result

	
    def differentiate(self, x, dim, n_deriv = 1, scalar = True): 
		'''
		Synopsis: returns the derivative of a spline of the given dimension
		about the point x.
		
		Return type: scalar/matrix

		x = the point of interest
		dim = dimension of b-spline you are differentiating
		basis = b-spline you are differentiating
		
		'''

		mat = self.basis(x, dim, scalar = False) #returns an Nxd matrix


		y = self.knots
		N = len(y)
		result = np.zeros((N, dim))

		# find the knot points that x lies between
		for i in xrange(N-1):
			if(x>y[i] and x<=y[i+1]): 
				place = i

		for i in xrange(dim,0,-1):

			basis = mat[:,(i-1)] 

			for j in xrange(place-i-1, place+1):
				result[j][i-1] = (i/(y[j+i] - y[j]))*basis[j] - (i/(y[j+i+1] - y[j+1]))*basis[j+1]
		
		if scalar:
			return result[place][dim - n_deriv]	
		else:
			return result
 
 
        
    def integrate_infinity(self, k, dim, x):
        '''
        Synopsis: returns the integral of the k-th spline of the given dimension
        from -infinity to x
        '''
        basis = self.basis(x, dim+1, scalar = False)[:,(dim+1)]
                
        y = self.knots
        N = len(y)
        
        result = 0
        for j in xrange(k, k+dim+1):
            result += basis[j]
        
        result *= (y[k+dim+1] - y[k])/(dim+1)
        
        return result


    def integrate(self, k, dim, a, b):
		'''
		Synopsis: returns the integral of the kth spline of the given dimension
		from a to b
		'''
		return (self.integrate_infinity(k, dim, b) - self.integrate_infinity(k, dim, a))
	
	
	#def integrate_double_prime_square(self, dim, k, l, a, b):
		
		

def makeBasis(knots):
    return SplineBasis(knots)