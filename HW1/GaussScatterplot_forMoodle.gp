sigma1= 2
sigma2= 1
rho= 0.5
siq1= sigma1**2;
siq2= sigma2**2;
lamba1= siq1
lamba2= siq2

if ( rho!= 0 ) {
  lamba1= 0.5*(  siq1 + siq2 + sqrt( (siq1+siq2)**2 - 4*siq1*siq2*(1-rho**2) )  ); 
  lamba2= 0.5*(  siq1 + siq2 - sqrt( (siq1+siq2)**2 - 4*siq1*siq2*(1-rho**2) )  );
}


ellipseMajor=  2 * log(2) * sqrt(lamba1)
ellipseMinor=  2 * log(2) * sqrt(lamba2)
ellipseAngleRad= atan(  sigma1 * sigma2 * rho / lamba1   )
ellipseAngle= ellipseAngleRad  * 180 / pi

n= 10000
array X[n];
array Y[n];

do for [i=1:n] {
    z1= invnorm( rand(0) );
    z2= invnorm( rand(0) );
    xraw= sigma1*z1;
    yraw= sigma2*(rho*z1 + z2*sqrt( 1 - rho*rho))

    X[i]= xraw; Y[i]= yraw;
};


set size ratio -1;

# Note: gnuplot ellipse size takes values 2a,2b.   for ellipse  x²/a² + y²/b² < 1
set object 1 ellipse center 0,0  size 2*ellipseMajor,2*ellipseMinor  angle ellipseAngle  front fillstyle empty border -1 lw 2

plot [-5:5][-5:5] X using (X[$1]):(Y[$1]) with dots notitle
