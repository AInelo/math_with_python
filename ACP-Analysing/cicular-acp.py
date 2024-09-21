# Importation des bibliothèques nécessaires
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Simulation des données : création d'un DataFrame avec des variables fictives
np.random.seed(0)  # Pour la reproductibilité
n_samples = 100
n_features = 5

data_simulated = pd.DataFrame({
    'Variable 1': np.random.rand(n_samples) * 10,
    'Variable 2': np.random.rand(n_samples) * 20,
    'Variable 3': np.random.rand(n_samples) * 30,
    'Variable 4': np.random.rand(n_samples) * 40,
    'Variable 5': np.random.rand(n_samples) * 50
})

# Normalisation des données
scaler = StandardScaler()
X_scaled = scaler.fit_transform(data_simulated)

# Appliquer l'ACP complète
pca_full = PCA(n_components=5)
X_pca_full = pca_full.fit_transform(X_scaled)

# Récupération des composantes principales
pcs = pca_full.components_

# Fonction pour tracer le cercle des corrélations
def plot_correlation_circle(pcs, n_components, pca, labels):
    fig, ax = plt.subplots(figsize=(8, 8))

    # Cercle de corrélation
    circle = plt.Circle((0, 0), 1, color='b', fill=False, linestyle='--', linewidth=1)
    ax.add_artist(circle)

    # Pour chaque variable initiale
    for i in range(len(labels)):
        # Les variables sont projetées sur les deux premières composantes
        plt.arrow(0, 0, pcs[n_components[0], i], pcs[n_components[1], i],
                  color='r', alpha=0.5, head_width=0.05, head_length=0.05)
        plt.text(pcs[n_components[0], i] * 1.15, pcs[n_components[1], i] * 1.15,
                 labels[i], color='g', ha='center', va='center')

    # Limites et étiquettes
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)
    plt.xlabel(f'Composante {n_components[0] + 1} ({pca.explained_variance_ratio_[n_components[0]]:.1%})')
    plt.ylabel(f'Composante {n_components[1] + 1} ({pca.explained_variance_ratio_[n_components[1]]:.1%})')
    plt.title('Cercle des corrélations')
    plt.grid(True)

    # Affichage du graphique
    plt.show()

# Noms des variables pour l'affichage
labels = ['Variable 1', 'Variable 2', 'Variable 3', 'Variable 4', 'Variable 5']

# Tracer le cercle des corrélations pour les deux premières composantes
plot_correlation_circle(pcs, [0, 1], pca_full, labels)
