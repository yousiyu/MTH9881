'''
Created on Oct 6, 2013

@author: ubuntu
'''

import Curves.BuildCurves as Curve
import Finance.DiscountFactor as DF
import Finance.FwdLiborRate as LR
import numpy as np
import scipy.optimize as optim
import matplotlib.pyplot as plt
import scipy.interpolate as interp


t = np.array([0.00,0.25,0.52,1.02,2.01,3.01,4.01,5.01,7.01,10.01,12.01,15.01,20.01,25.01,30.01])
lib_rate = np.array([0.0054588,0.0054625,0.0068780,0.0070480,0.0069000,0.0079800,0.0100800,0.0124800,0.0169000,0.0210600,0.0229800,0.0247800,0.0259900,0.0265950,0.0269400])
ois_rate = np.array([0.0007000,0.0008745,0.0019530,0.0017980,0.0016000,0.0028170,0.0051550,0.0078550,0.0127620,0.0176100,0.0198050,0.0218920,0.0234400,0.0242570,0.0247520])

knots = np.array([0.1, 0.3, 0.8, 1.6, 3.1, 5.1, 7.1, 10.1, 15.1, 20.1, 29.1])

res = Curve.BuildCurves(0,knots,t,ois_rate, lib_rate)

ois_tck = res[0]
lib_tck = res[1]

plt.plot(t, interp.splev(t,ois_tck)), plt.show()
plt.plot(t, interp.splev(t,lib_tck)), plt.show()
plt.plot(t, interp.splev(t,lib_tck) - interp.splev(t,ois_tck)), plt.show()




# x = np.linspace(0, 30, 50)
# 
# dfs = np.zeros(len(x))
# fwd = np.zeros(len(x))
# 
# for i in xrange(len(x)):
#     dfs[i] = DF.DiscountFactor(res[0], 0, x[i])
#     fwd[i] = LR.FwdLiborRate(res[1], 0, x[i], 0.25) 
# 
# plt.plot(x,dfs), plt.show()
# plt.plot(x,fwd), plt.show()

