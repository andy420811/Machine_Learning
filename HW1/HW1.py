import math
import numpy as np
from scipy import rand
from scipy.stats import norm
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox , oy = origin
    px = point[0]
    py = point[1]

    qx = [ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy) for px,py in zip(px,py)]
    qy = [oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy) for px,py in zip(px,py)]
    return qx, qy
def inside_probability(x , y , a , b , n):
  count = 0
  for x,y in zip(x,y):
    if (x**2)/(a**2) + (y**2)/(b**2) <= 1 :
      count += 1
  return count/n

sigma1= 2
sigma2= 1
rho= 0.5
siq1= sigma1**2
siq2= sigma2**2
lamba1= siq1
lamba2= siq2

if ( rho!= 0 ) :
  lamba1= 0.5*(  siq1 + siq2 + math.sqrt( (siq1+siq2)**2 - 4*siq1*siq2*(1-rho**2) )  )
  lamba2= 0.5*(  siq1 + siq2 - math.sqrt( (siq1+siq2)**2 - 4*siq1*siq2*(1-rho**2) )  )



ellipseMajor=  2 * math.log(2) * math.sqrt(lamba1)
ellipseMinor=  2 * math.log(2) * math.sqrt(lamba2)
ellipseAngleRad= math.atan(  sigma1 * sigma2 * rho / lamba1   )
ellipseAngle= ellipseAngleRad  * 180 / math.pi

n= 10000
X = list()
Y = list()
count = 0

for i in range(n) :
    z1= norm.ppf( np.random.rand() )
    z2= norm.ppf( np.random.rand() )
    xraw= sigma1*z1
    yraw= sigma2*(rho*z1 + z2*math.sqrt( 1 - rho*rho))
    X.append(xraw)
    Y.append(yraw)
    


ax = plt.subplot(211)
ellipse = Ellipse(xy=(0,0), width=2*ellipseMajor, height=2*ellipseMinor, 
                        edgecolor='r', fc='None', lw=2,angle=ellipseAngle)
ax.add_patch(ellipse)
# confidence_ellipse.confidence_ellipse(np.array(X), np.array(Y), ax, n_std=1,
#                  label=r'$1\sigma$', edgecolor='firebrick')

plt.scatter(X,Y,0.03)

ax = plt.subplot(212)
ellipse = Ellipse(xy=(0,0), width=2*ellipseMajor, height=2*ellipseMinor, 
                        edgecolor='r', fc='None', lw=2,angle=0)
ax.add_patch(ellipse)
# confidence_ellipse.confidence_ellipse(np.array(X), np.array(Y), ax, n_std=1,
#                  label=r'$1\sigma$', edgecolor='firebrick')
rx , ry = rotate([0,0],[X,Y],-ellipseAngleRad)
plt.scatter(rx , ry , 0.03)
p = inside_probability(rx,ry,ellipseMajor,ellipseMinor,n)
print("Pr = {}".format(p))

plt.show()
# Note: gnuplot ellipse size takes values 2a,2b.   for ellipse  x�/a� + y�/b� < 1

