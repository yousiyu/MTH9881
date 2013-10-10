import scipy.interpolate as interp
import scipy.optimize as optim


def ObjectiveFunction(sigma, knots, ts, ois_rate, lib_rate):
	"""
	constructs the B-spline for the given knots, times( in years), 
	OIS rates, and LIBOR rates for the corresponding times. Calculates
	the objective function for the given parameters.
	
	
	sigma = float (lambda from equation (40) on page 23 of lecture 1 notes)
	knots = numpy array
	ts = numpy array
	ois_rate = numpy array
	lib_rate = numpy array
	"""
		
	tck1 = interp.splrep(ts, ois_rate, t = knots)
	tck2 = interp.splrep(ts, lib_rate, t = knots)
	
	approx1 = interp.splev(ts,tck1)
	approx2 = interp.splev(ts,tck2)
	
	partial_sum = ((approx1 - ois_rate)**2).sum()
	partial_sum += (sum((approx2 - lib_rate)**2)).sum()
	partial_sum *= 0.5
		
	new_tck = []
	new_tck.append(knots)
	new_tck.append((interp.splev(ts,tck1,der=2))**2 + (interp.splev(ts, tck2, der=2)**2))
	new_tck.append(3)
	
	temp = interp.splint(ts[0], ts[-1], new_tck)
		
	partial_sum += 0.5*sigma*temp
	
	return partial_sum



def BuildCurves(params, knots, ts, ois_rate, lib_rate):
	"""
	Constructs the OIS and LIBOR curves using B-splines with the 
	given set of interior knot points and times t.
	
	Params = 2-element list [sigma, s]
	knots = numpy array
	ts = numpy array
	ois_rate = numpy array
	lib_rate = numpy array
	"""
	
	#func = lambda x: ObjectiveFunction(x, knots, ts, ois_rate, lib_rate)
	#bnds = [(0,None)]
	
	#calculate the optimal parameter lambda
	#res = optim.minimize(func, params, method = 'L-BFGS-B', bounds = bnds, tol = 1e-4) 
	
	#return the coefficients of the splines
	tck1 = interp.splrep(ts,ois_rate, t = knots)
	tck2 = interp.splrep(ts,lib_rate, t = knots)

	return (tck1,tck2)



