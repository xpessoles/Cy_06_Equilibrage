import numpy as np
import matplotlib.pyplot as plt

E3=0
D3=10**(-4) 
m3=10
b=0.05*1e-3 
g=9.81
omega=30000*2*np.pi/60
T=2*np.pi/omega
t=np.linspace(0,T,100)
theta=omega*t

L=omega**2*(D3*np.cos(theta)+E3*np.sin(theta))
M=omega**2*(D3*np.sin(theta)-E3*np.cos(theta))

X=b*m3*omega**2*np.sin(theta)
Y=-m3*g-b*m3*omega**2*np.cos(theta)

plt.figure(1)
plt.plot(t,L,'r-',label='$L_{03}$')
plt.plot(t,M,'b-',label='$M_{03}$')
plt.xlabel('Temps en s')
plt.ylabel('Moments en N.m')
plt.legend()
plt.savefig('moment.eps')

plt.figure()
plt.plot(t,X,'r-',label='$X_{03}$')
plt.plot(t,Y,'b-',label='$Y_{03}$')
plt.xlabel('Temps en s')
plt.ylabel('Effort en N')
plt.legend()
plt.savefig('effort.eps')
plt.show()