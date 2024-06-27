import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Exemple de données
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 1, 0, 1, 0, 1])

# Création du modèle d'interpolation par spline cubique
cs = CubicSpline(x, y)

# Points pour évaluer la spline
x_new = np.linspace(x.min(), x.max(), 100)
y_new = cs(x_new)

# Visualisation
plt.plot(x, y, 'o', label='Données originales')
plt.plot(x_new, y_new, label='Spline cubique')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolation par spline cubique')
plt.show()
