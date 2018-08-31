from math import exp, log, sqrt
from numpy import roots
def pr_fug (z, A, B):
   r2 = sqrt(2)
   arg = z-1-log(z-B)-A/(2*r2*B)*log((z+(1+r2)*B)/(z+(1-r2)*B))
   return exp(arg)
Tc = 425.2
Pc = 38.0
omega = 0.199
ep = 1.e-6
maxiter = 1000
P = 1
T = 298.15
kappa = 0.37464 + 1.54226*omega - 0.26992*omega*omega
crit = 0
niter = 0
while ( abs(1-crit) > ep and niter < maxiter ):
   A = 0.45724*(P/Pc)*(Tc/T)**2*(1+kappa*(1-(T/Tc)**(0.5)))**2
   B = 0.07780*(Tc/T)*(P/Pc)
   coeff = [ 1, -1 + B, A - 3*B*B - 2*B, -A*B + B*B + B*B*B ]
   Z = roots(coeff)
   ZV = Z[0].real
   ZL = 0
   if ( Z[2].imag != 0 ):
      print "Only one root found"
      exit()
   else:
      ZL = Z[2].real
   crit = pr_fug(ZL,A,B)/pr_fug(ZV,A,B)
   P = P * crit
   print "iter = {0:d}, Pressure = {1:.8f} bar".format(niter,P)
   niter = niter + 1
print "Pvap = {0:0.8f} bar".format(P)
print "Program ends."

