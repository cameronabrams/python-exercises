Tc = 425.2
Pc = 38.0
omega = 0.199

P = 1
T = 298.15

kappa = 0.37464 + 1.54226*omega - 0.26992*omega*omega
A = 0.45724*(P/Pc)*(Tc/T)**2*(1+kappa*(1-(T/Tc)**(0.5)))**2
B = 0.07780*(Tc/T)*(P/Pc)

print "A = {0:.8f}, B = {1:.8f}".format(A,B)
print "Program ends."

