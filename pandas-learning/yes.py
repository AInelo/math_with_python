import numpy as np
import matplotlib.pyplot as plt

# Générer des données pour les fonctions cosinus et sinus
x = np.linspace(-2*np.pi, 2*np.pi, 400)  # Créer un tableau de valeurs x de -2π à 2π
y_cos = np.cos(x)  # Calculer les valeurs de cos(x)
y_sin = np.sin(x)  # Calculer les valeurs de sin(x)

# Tracer les courbes
plt.plot(x, y_cos, label='cos(x)')  # Tracer cos(x)
plt.plot(x, y_sin, label='sin(x)')  # Tracer sin(x)

# Ajouter un titre et une légende
plt.title("Tracé des fonctions cosinus et sinus")
plt.legend()

# Afficher le graphique
plt.show()
