import control as ct
import numpy as np
import matplotlib.pyplot as plt


def afficheperform(bo_nc, bo_c, wc):
    # Vérification des performances de l'asservissement
    # afficheperform(bo_nc, bo_c, wc)
    # bo_nc : boucle ouverte non corrigée
    # bo_c : boucle ouverte corrigée
    # wc : pulsation de coupure imposée
    _, Ph, _ = ct.frequency_response(bo_nc, wc)
    _, pm, _, _ = ct.margin(bo_c)
    fig = plt.figure()
    ct.bode_plot(bo_nc, None, 'r', dB=True,
                 label='BO non corrigée', legend_loc='upper right')
    ct.bode_plot(bo_nc, wc, 'ro', dB=True,
                 label=f'$\\Delta\\phi_S$={180.0+Ph[0]*180.0/np.pi:.2f}°', legend_loc='upper right')
    ct.bode_plot(bo_c, None, 'b', dB=True,
                 label='BO corrigée', legend_loc='upper right')
    ct.bode_plot(bo_c, wc, 'bo', dB=True,
                 label=f'$\\Delta\\phi$= {pm:.2f}°', legend_loc='upper right')
    plt.grid(True)
    fig.get_axes()[0].set_title(f'$\\omega_c$ = {wc:.2f} rd/s')
    plt.figure()
    data = ct.step_response(ct.feedback(bo_c, 1))
    ct.time_response_plot(data, title='Réponse indicielle avec correcteur')
    plt.grid(True)
    plt.show()


def corrprop(bo_pos, wc):
    # Réglage d'un correcteur proportionnel
    # corrprop(bo_pos, wc)
    # Paramètres
    # bo_pos : boucle ouverte non corrigée
    # wc : pulsation de coupure imposée
    # Retour
    # K : gain du correcteur C(p)=K
    Ga, _, _ = ct.frequency_response(bo_pos, wc)
    K = 1/Ga[0]
    print('-- Correction proportionnelle')
    print(f'K = {K:.2f}')
    return K


def corravph(bo_pos, wc, mp):
    # Réglage d'un correcteur à avance de phase
    # corravph(bo_pos, wc, mp)
    # Paramètres
    # bo_pos : boucle ouverte non corrigée
    # wc : pulsation de coupure imposée
    # mp : marge de phase imposée
    # Retour
    # a, T, K : paramètres du correcteur C(p)=K(1+Tp)/(1+aTp)
    Ga, Ph, omega = ct.frequency_response(bo_pos, wc)
    Ph = Ph[0]*180.0/np.pi
    mpC = mp-(180+Ph)
    a = (1-np.sin(np.pi*mpC/180))/(1+np.sin(np.pi*mpC/180))
    T = 1/(wc*np.sqrt(a))
    K = np.sqrt(a)/Ga[0]
    print('-- Correction par avance de phase')
    print(f'a = {a:.3f}  T = {T:.3f}  K = {K:.3f}')
    return a, T, K


def corrpara(bo_vit, wc, mp):
    # Réglage d'un correcteur tackymétrique
    # corrpara(bo_vit, wc, mp)
    # Paramètres
    # bo_vit : boucle ouverte en vitesse
    # wc : pulsation de coupure imposée
    # mp : marge de phase imposée
    # Retour
    # K_omega : gain en retour sur la boucle ouverte en vitesse
    # (il convient ensuite d'utiliser la fonction corrprop pour obtenir le gain K_theta)
    Ga, Ph, omega = ct.frequency_response(bo_vit, wc)
    Ph = Ph[0]*180.0/np.pi
    K_omega = -np.cos(np.pi*(Ph-mp)/180)/(Ga[0]*np.cos(np.pi*mp/180))
    print('-- Correction parallèle')
    print(f'K_omega = {K_omega:.2f}')
    return K_omega
