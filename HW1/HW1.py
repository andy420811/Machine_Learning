import math as Math
import numpy as np
from scipy import rand
from scipy.stats import norm
import matplotlib.pyplot as plt

sigma1= 2
sigma2= 1
rho= 0.5
siq1= sigma1**2
siq2= sigma2**2
lamba1= siq1
lamba2= siq2

if ( rho!= 0 ) :
  lamba1= 0.5*(  siq1 + siq2 + Math.sqrt( (siq1+siq2)**2 - 4*siq1*siq2*(1-rho**2) )  )
  lamba2= 0.5*(  siq1 + siq2 - Math.sqrt( (siq1+siq2)**2 - 4*siq1*siq2*(1-rho**2) )  )



ellipseMajor=  2 * Math.log10(2) * Math.sqrt(lamba1)
ellipseMinor=  2 * Math.log10(2) * Math.sqrt(lamba2)
ellipseAngleRad= Math.atan(  sigma1 * sigma2 * rho / lamba1   )
ellipseAngle= ellipseAngleRad  * 180 / Math.pi

n= 10000
X = list()
Y = list()

for i in range(n) :
    z1= norm.ppf( np.random.rand() )
    z2= norm.ppf( np.random.rand() )
    xraw= sigma1*z1
    yraw= sigma2*(rho*z1 + z2*Math.sqrt( 1 - rho*rho))
    X.append(xraw)
    Y.append(yraw)
    


plt.scatter(X,Y,0.03)

# Note: gnuplot ellipse size takes values 2a,2b.   for ellipse  x�/a� + y�/b� < 1

