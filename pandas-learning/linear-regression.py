import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Données
x = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 3, 5, 7, 11])

# Modèle de régression
model = LinearRegression()
model.fit(x, y)

# Prédictions
y_pred = model.predict(x)

# Tracer les données et la ligne de régression
plt.scatter(x, y, color='blue', label='Données')
plt.plot(x, y_pred, color='red', label='Ligne de régression')
plt.xlabel("Variable indépendante (x)")
plt.ylabel("Variable dépendante (y)")
plt.title("Régression linéaire simple")
plt.legend()
plt.show()

# Afficher les coefficients
print(f"Ordonnée à l'origine (intercept): {model.intercept_}")
print(f"Coefficient de régression (slope): {model.coef_[0]}")
