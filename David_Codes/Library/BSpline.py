'''
Created on Sep 22, 2013

@author: David Herssein
'''

import numpy as np


class Bspline(object):
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
    
    
    
    def differentiate_b_spline(self, x, dim): 
        """
        Synopsis: returns the derivative of a spline of the given dimension
        about the point x.
        """
        spline = self.b_spline(x, dim-1, False)
        
        y = self.knots
        N = len(y)
        result = np.zeros(N)
        
        # find the knot points that x lies between
        for i in range(N-1):
            if(x>y[i] and x<=y[i+1]): 
                place = i
        
        i = dim
        for j in range(place-i-1, place+1):
            result[j] = (dim/(y[j+i] - y[j]))*spline[j] - (dim/(y[j+i+1] - y[j+1]))*spline[j+1]
    
        return result[place]
    
    
    
    def integrate_b_spline(self, x, dim):
        """
        Synopsis: returns the derivative of a spline of the given dimension
        about the point x.
        """
        spline = self.b_spline(x, dim+1, scalar = False)
        
        y = self.knots
        N = len(y)
        
        # find the knot points that x lies between
        for i in range(N-1):
            if(x>y[i] and x<=y[i+1]): 
                place = i
        
        result = 0
        for j in range(place-dim, place+1):
            result += (y[place+dim+1] - y[place])/(dim+1)*spline[j]
    
        return result
    
    
    
    def b_spline(self, x, dim = 3, scalar = True):
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
        for i in range(N-1):
            if(x>y[i] and x<=y[i+1]): 
                result[i][0] = 1
                place = i
        
        for i in range(1,d):
            for j in range(place-i-1, place+1):
                result[j][i] = ((x - y[j])/(y[j+i] - y[j]))*result[j][i-1] + ((y[j+i+1]-x)/(y[j+i+1] - y[j+1]))*result[j+1][i-1]
    
    	if(scalar): 
    		return result[place,dim]
    	else: 
    		return result[:,dim]
    
    

def makeSpline(knots):
    return Bspline(knots)