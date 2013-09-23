import numpy as np


class Bspline(object):
    '''
    classdocs
    '''


    def __init__(self, knots):
        '''
        Constructor
        '''
        self.knots = knots
    
    
    
    def differentiate_b_spline(self, x, dim): 

        spline = self.b_spline(x, dim-1)
        
        y = self.knots
        N = len(y)
        result = np.zeros(N)
        
        # find the knot points that x lies between
        for i in range(N-1):
            if(x>=y[i] and x<=y[i+1]): 
                place = i
        
        i = dim
        for j in range(place-i-1, place+1):
            result[j] = (dim/(y[j+i] - y[j]))*spline[j] - (dim/(y[j+i+1] - y[j+1]))*spline[j+1]
    
        return result
    
    
    
    def integrate_b_spline(self):
        pass
    
    
    
    def b_spline(self, x, dim = 3):
        '''
        x is a number
        d is the order of the b-spline
        '''
        y = self.knots
        
        d = dim+1
        N = len(y)
        result = np.zeros((N,d))
        
        # find the knot points that x lies between
        for i in range(N-1):
            if(x>=y[i] and x<=y[i+1]): 
                result[i][0] = 1
                place = i
        
        for i in range(1,d):
            for j in range(place-i-1, place+1):
                result[j][i] = ((x - y[j])/(y[j+i] - y[j]))*result[j][i-1] + ((y[j+i+1]-x)/(y[j+i+1] - y[j+1]))*result[j+1][i-1]
    
        return result[:,dim]
