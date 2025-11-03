import control as ct
import numpy as np
import matplotlib.pyplot as plt
from regl_corr import afficheperform, corrprop, corravph, corrpara

# Définir une fonction de transfert
p = ct.tf('s')
Hv = 100/((1+p/100)*(1+p/1000))
H = Hv/p
out = ct.bode_plot(H, dB=True, title='Réponse harmonique')
plt.show()

# Cahier des charges commun
wc = 200
mp = 57

# Correcteur à avance de phase
a, T, K = corravph(H, wc, mp)
CAVP = K*(1+T*p)/(1+a*T*p)
afficheperform(H, CAVP*H, wc)

# Correcteur tackymétrique
K_omega = corrpara(Hv, wc, mp)
Hvf = ct.feedback(Hv, K_omega)
Hp = Hvf/p
K_theta = corrprop(Hp, wc)
Hp = K_theta*Hvf/p
afficheperform(Hv/p, Hp, wc)


# Exemple de prise en compte d'une perturbation
def e(t):
    return 1.0*(t >= 0.01)


def d(t):
    return 0.8*(t >= 0.1)


T = np.arange(0, 0.2, 0.0001)
Hvf = ct.feedback(Hv, K_omega)
Hey = ct.feedback(K_theta*Hvf/p, 1)
Hdy = ct.feedback(Hvf/p, K_theta)
dataey = ct.forced_response(Hey, T, e(T))
datady = ct.forced_response(Hdy, T, d(T))

plt.figure()
plt.plot(T, dataey[1]+datady[1], 'b', label='$V_\\theta(t)$')
plt.plot(T, e(T), 'r--', label='$e(t)$', lw=1)
plt.plot(T, d(T), 'g--', label='$d(t)$', lw=1)
plt.legend()
plt.ylabel('$V_\\theta(t)$')
plt.xlabel('$t$')
plt.grid(True)
plt.show()
