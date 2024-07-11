import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Générer des données aléatoires
np.random.seed(0)  # Pour rendre les résultats reproductibles
x = 2 * np.random.rand(100, 1)
y = 4 + 3 * x + np.random.randn(100, 1)

# Créer le modèle de régression linéaire
model = LinearRegression()
model.fit(x, y)

# Prédire les valeurs de y pour les valeurs de x
x_new = np.linspace(0, 2, 100).reshape(100, 1)
y_predict = model.predict(x_new)

# Tracer les données et la ligne de régression
plt.scatter(x, y, color='blue', label='Données')
plt.plot(x_new, y_predict, color='red', label='Ligne de régression')
plt.xlabel("Variable indépendante (x)")
plt.ylabel("Variable dépendante (y)")
plt.title("Régression linéaire simple")
plt.legend()
plt.show()

# Afficher les coefficients de la régression
print(f"Ordonnée à l'origine (intercept): {model.intercept_[0]}")
print(f"Coefficient de régression (slope): {model.coef_[0][0]}")
