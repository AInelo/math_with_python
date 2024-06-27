import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Paramètres du modèle
alpha = 0.3
delta = 0.05
n = 0.01
r = 0.03
t = 0.2

# Fonction de production Cobb-Douglas
def f(k):
    return k**alpha

# Système d'équations différentielles
def system(y, t):
    k, lambda_ = y
    i = (1 + n) / lambda_  # Investissement optimal à partir de la condition d'optimalité
    dot_k = (1 + delta) / (1 - n) * k + i / (1 + n) - k  # Dynamique du capital
    dot_lambda = -(1 - t) * alpha * k**(alpha - 1) - lambda_ * (1 + delta) / (1 - n)  # Dynamique du multiplicateur de Lagrange
    return [dot_k, dot_lambda]

# Conditions initiales
k0 = 1  # Capital initial
lambda0 = 1 + n  # Valeur initiale du multiplicateur de Lagrange
y0 = [k0, lambda0]

# Intervalle de temps
time = np.linspace(0, 100, 200)  # De 0 à 100 périodes

# Résolution numérique
solution = odeint(system, y0, time)

# Extraction des solutions pour k et lambda
k_sol = solution[:, 0]
lambda_sol = solution[:, 1]

# Affichage des résultats
plt.plot(time, k_sol, label='Capital (k)')
plt.plot(time, lambda_sol, label='Multiplicateur de Lagrange (λ)')
plt.legend()
plt.xlabel('Temps')
plt.ylabel('Valeurs')
plt.title('Dynamique du capital et du multiplicateur de Lagrange')
plt.show()
