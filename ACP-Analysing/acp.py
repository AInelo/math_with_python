# Importation des bibliothèques nécessaires
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Simulation des données : création d'un DataFrame avec des variables fictives
np.random.seed(0)  # Pour la reproductibilité
n_samples = 100
n_features = 5

# Simuler des données aléatoires avec une corrélation
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

# Appliquer l'ACP
pca = PCA(n_components=2)  # Nous réduisons à 2 dimensions pour visualiser
X_pca = pca.fit_transform(X_scaled)

# Récupérer la variance expliquée par chaque composante
explained_variance = pca.explained_variance_ratio_

# Création des graphiques
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Graphique de projection des données dans le plan ACP
axes[0].scatter(X_pca[:, 0], X_pca[:, 1], c='blue', edgecolor='k', s=50)
axes[0].set_xlabel('Première composante principale')
axes[0].set_ylabel('Deuxième composante principale')
axes[0].set_title('ACP : Projection des données')
axes[0].grid(True)

# Graphique de la variance expliquée cumulée
axes[1].plot(range(1, len(explained_variance)+1), explained_variance.cumsum(), marker='o', linestyle='--')
axes[1].set_title('Variance expliquée cumulée')
axes[1].set_xlabel('Nombre de composantes principales')
axes[1].set_ylabel('Variance expliquée cumulée')
axes[1].grid(True)

# Afficher les graphiques
plt.tight_layout()
plt.show()

# Résultats d'ACP : Variance expliquée
explained_variance