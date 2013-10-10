'''
Created on Oct 7, 2013

@author: ubuntu
'''

from scipy.interpolate import splint
import math

def FwdLiborRate(tck, S, T):
    """
    This function calculates the LIBOR forward rate (as seen today) from 
    time S to time T.
    
    tck should be the output from splrep
    S is a float
    T is a float
    """
    l = tck[1]
    
    psum = sum(splint(S, T, tck)*l, 0)
    return (1.0/(T-S))*(math.exp(psum) - 1)
    
    
    
    