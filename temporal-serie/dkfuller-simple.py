import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

# Génération d'une série temporelle avec une tendance déterministe
np.random.seed(0)
t = np.arange(100)
y = 2 + 0.5 * t + np.random.normal(0, 1, size=t.shape)

# Affichage de la série temporelle
plt.figure(figsize=(10, 5))
plt.plot(t, y, label='Série Temporelle')
plt.xlabel('Temps')
plt.ylabel('Valeur')
plt.title('Série Temporelle avec Tendance')
plt.legend()
plt.show()

# Exécution du test de Dickey-Fuller
result = adfuller(y)
print('Statistique ADF:', result[0])
print('p-value:', result[1])
print('Valeurs Critiques:', result[4])

if result[1] < 0.05:
    print("La série est stationnaire (rejette l'hypothèse nulle).")
else:
    print("La série n'est pas stationnaire (ne rejette pas l'hypothèse nulle).")
