import numpy as np
import matplotlib.pyplot as plt

# Paramètres
taille = 1000  # Nombre de points
moyenne = 100
ecart_type = 1

# Génération du bruit blanc gaussien
bruit = np.random.normal(moyenne, ecart_type, taille)

# Création de la figure
plt.figure(figsize=(10, 6))

# Affichage du bruit en fonction du temps
plt.subplot(1, 2, 1)
plt.plot(bruit, label='Bruit blanc gaussien')
plt.title('Signal de Bruit Blanc Gaussien')
plt.xlabel('Temps')
plt.ylabel('Amplitude')
plt.legend()

# Affichage de l'histogramme du bruit
plt.subplot(1, 2, 2)
plt.hist(bruit, bins=30, density=True, alpha=0.6, color='g')
plt.title('Histogramme du Bruit Blanc Gaussien')
plt.xlabel('Amplitude')
plt.ylabel('Densité')

# Affichage des graphiques
plt.tight_layout()
plt.show()
