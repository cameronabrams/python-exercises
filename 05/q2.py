from numpy import roots

Tc = 425.2
Pc = 38.0
omega = 0.199

P = 1
#T = 298.15
T= 800
kappa = 0.37464 + 1.54226*omega - 0.26992*omega*omega
A = 0.45724*(P/Pc)*(Tc/T)**2*(1+kappa*(1-(T/Tc)**(0.5)))**2
B = 0.07780*(Tc/T)*(P/Pc)
coeff = [ 1, -1 + B, A - 3*B*B - 2*B, -A*B + B*B + B*B*B ]
Z = roots(coeff)

ZV = Z[0].real
ZL = 0

if ( Z[2].imag != 0 ):
   print "Only one root found"
else:
   ZL = Z[2].real

print "A = {0:.8f}, B = {1:.8f}".format(A,B)
print "ZV = {0:.8f}, ZL = {1:.8f}".format(ZV,ZL)
print "Program ends."

