from math import exp, log, sqrt
from numpy import roots
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
def pr_fug (z, A, B):
   r2 = sqrt(2)
   arg = z-1-log(z-B)-A/(2*r2*B)*log((z+(1+r2)*B)/(z+(1-r2)*B))
   return exp(arg)
lab='ammonia'
Tc = 405.5
Pc =113.5
omega = 0.250
ep = 1.e-6
maxiter = 1000
P = 1
T = 150
dT = 10
kappa = 0.37464 + 1.54226*omega - 0.26992*omega*omega
T_list=[]
P_list=[]
ZL=ep
while ( ZL > 0 and T < Tc ):
   crit = 0
   niter = 0
   while ( ZL > 0 and abs(1-crit) > ep and niter < maxiter ):
      A = 0.45724*(P/Pc)*(Tc/T)**2*(1+kappa*(1-(T/Tc)**(0.5)))**2
      B = 0.07780*(Tc/T)*(P/Pc)
      coeff = [ 1, -1 + B, A - 3*B*B - 2*B, -A*B + B*B + B*B*B ]
      Z = roots(coeff)
      ZV = Z[0].real
      if ( Z[2].imag != 0 ):
         ZL = 0
      else:
         ZL = Z[2].real
      if ( ZL > 0 ):
         crit = pr_fug(ZL,A,B)/pr_fug(ZV,A,B)
         P = P * crit
         niter = niter + 1
   if ( ZL > 0 ):
      print "T = {0:.3f} K, P = {1:.8f} bar".format(T,P)
      T_list.append(1.0/T)
      P_list.append(log(P))
      T = T + dT

plt.plot(T_list,P_list,label=lab)
plt.legend()
plt.ylabel('ln Pvap(bar)')
plt.xlabel('1/T(K)')
plt.ylim([-20,5])
plt.xlim([0.002,0.010])
plt.savefig("my-ammonia.png")
