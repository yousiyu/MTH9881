'''
Created on Oct 6, 2013

@author: ubuntu
'''

from scipy.interpolate import splint
import math

def DiscountFactor(tck, S, T):
    """
    This function calculates the discount factor (as seen today) from 
    time S to time T.
    
    tck should be the output from splrep
    S is a float
    T is a float
    """
    f = tck[1]
    
    psum = sum(splint(S, T, tck)*f, 0)
    return math.exp(-psum)
    
    
    
    
    
    
    
    
    