import BSpline

def forward_ON_rate(t, ts, knots, rates, coeffs):
    basis = BSpline.makeBasis(knots)
    y = basis.basis(t, dim = 3, scalar = False)
    #print y
    result = 0.0
    
    for i in range(len(rates)):
    	#result += rates[i]*y[i+3]
        	
    	#find k for corresponding ts[i]
    	for j in range(len(knots)-1): 
    		if(ts[i] > knots[j] and ts[i] <= knots[j+1]):
    			result += rates[i]*y[j-1]

    return result