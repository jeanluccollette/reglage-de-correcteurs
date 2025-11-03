# Réglage de correcteurs

## Cahier des charges

On souhaite obtenir une **réponse indicielle en boucle fermée** qui soit approximativement associée à un dépassement $D$ et à un temps de premier maximum $t_m$. On en déduit des contraintes sur la **réponse harmonique en boucle ouverte** sous la forme d'une pulsation de coupure $\omega_c$ et d'une marge de phase $\Delta\Phi$. Les abaques ci-dessous donnent le lien approximatif entre ces différentes grandeurs. Il est courant de faire l'approximation supplémentaire $\omega_c \times t_m \approx 3$ pour obtenir ces contraintes. La recherche sur les définitions de ces grandeurs est laissée au soin du lecteur.

![](abaque1.png)

![](abaque2.png)

Dans les exemples qui suivent, on souhaite $t_m \approx 15 \text{ms}$ et $D \approx 10 \text{\\%}$. Il en résulte que $\omega_c=200\text{rd/s}$ et $\Delta\Phi=57\text{°}$.

## Exemple choisi pour illustrer les réglages

Le système étudié est un moteur à courant continu commandé par la tension à ses bornes. On dispose par ailleurs d'une mesure de la position et de la vitesse angulaire. Pour simplifier, on considère que ces mesures correspondent aux grandeurs physiques elles-mêmes. Dans la réalité, il faudra prendre en compte le gain des capteurs délivrant une valeur proportionnelle à ces grandeurs physiques.

Ce système est caractérisé par la fonction de transfert

$$\mu(p)=\dfrac{\Omega(p)}{U(p)}$$

Pour compléter l'étude, on évalue l'effet d'une perturbation $d(t)$ sous forme d'échelon.

## Les programmes

Le programme [regl_corr.py](regl_corr.py) rassemble des fonctions réalisant le calcul des coefficients pour différents correcteurs et la validation de leur fonctionnement. Le programme [test_regl_corr.py](test_regl_corr.py) fait appel à ces fonction pour une fonction de transfert $\mu(p)$ imposée. Ces programmes utilisent le package [control](https://python-control.readthedocs.io/en/0.10.1/) (on choisira de préférence la version 0.10.1).

## Correction série (avance de phase)

Le cahier des charges imposé ($\omega_c=200\text{rd/s}$ et $\Delta\Phi=57\text{°}$) aboutit aux valeurs ci-dessous pour les paramètres d'un correcteur à avance de phase. On considère ici que $d(t)=0$.

```console
-- Correction par avance de phase
a = 0.201  T = 0.011  K = 2.043
```

![](Diapositive1.PNG)

Le réglage est validé par le tracé de la réponse harmonique en boucle ouverte corrigée.

![](Figure_1.png)

Avec le tracé de la réponse indicielle en boucle fermée, on vérifie que $t_m \approx 15 \text{ms}$ et $D \approx 10 \text{\\%}$.

![](Figure_2.png)

## Correction tackymétrique

Le cahier des charges imposé ($\omega_c=200\text{rd/s}$ et $\Delta\Phi=57\text{°}$) aboutit aux valeurs ci-dessous pour les paramètres d'un correcteur tackymétrique.

```console
-- Correction parallèle
K_omega = 0.03
-- Correction proportionnelle
K = 8.08
```

Le calcul s'effectue en deux temps. Le gain $K_\Omega$ assure que la réponse harmonique du système bouclé en vitesse présente le déphasage à $\omega_c$ qui corresponde bien à la marge de phase $\Delta\Phi$ imposée. Ensuite,  $K_\theta$ (correction proportionnelle sur le système bouclé en vitesse) est le gain assurant que la pulsation de coupure soit bien celle qui est imposée.

![](Diapositive2.PNG)

Le réglage est validé par le tracé de la réponse harmonique en boucle ouverte corrigée.

![](Figure_3.png)

Avec le tracé de la réponse indicielle en boucle fermée, on vérifie que $t_m \approx 15 \text{ms}$ et $D \approx 10 \text{\\%}$.

![](Figure_4.png)

Sur cet exemple, on peut par ailleurs étudier l'incidence d'une perturbation $d(t)$. On constate alors l'apparition d'un erreur statique entre la consigne et la mesure. L'élimination de cette erreur statique nécessitera l'ajout d'une correction avec action intégrale qui demandera un ajustement des paramètres du correcteur tackymétrique.

![](Figure_5.png)
