# Réglage de correcteurs

## Cahier des charges

On souhaite obtenir une **réponse indicielle en boucle fermée** qui soit approximativement associée à un dépassement $D$ et à un temps de premier maximum $t_m$. On en déduit des contraintes sur la **réponse harmonique en boucle ouverte** sous la forme d'une pulsation de coupure $\omega_c$ et d'une marge de phase $\Delta\Phi$. Les abaques ci-dessous donnent le lien entre ces différentes grandeurs. Il est courant de faire l'approximation $\omega_c \times t_m \approx 3$ pour obtenir ces contraintes.

![](abaque1.png)

![](abaque2.png)

Dans les exemples qui suivent, on souhaite $t_m \approx 15 \text{ms}$ et $D \approx 10 \text{\\%}$. Il en résulte que $\omega_c=200\text{rd/s}$ et $\Delta\Phi=57\text{°}$.

## Exemple choisi pour illustrer les réglages

Le système étudié est un moteur à courant continu commandé par la tension à ses bornes. On dispose par ailleurs d'une mesure de la position et de la vitesse angulaire. Ce système est caractérisé par la fonction de transfert

$$\mu(p)=\dfrac{\Omega(p)}{U(p)}$$

## Correction série (avance de phase)

![](Diapositive1.PNG)

![](Figure_1.png)

![](Figure_2.png)

## Correction tackymétrique

![](Diapositive2.PNG)

![](Figure_3.png)

![](Figure_4.png)

![](Figure_5.png)
