import numpy as np
from sklearn.linear_model import LinearRegression

# Données
X = np.array([[1, 1], [2, 1], [3, 2], [4, 3], [5, 3]])
y = np.array([2, 3, 5, 7, 11])

# Modèle de régression
model = LinearRegression()
model.fit(X, y)

# Prédictions
y_pred = model.predict(X)

# Afficher les coefficients
print(f"Ordonnée à l'origine (intercept): {model.intercept_}")
print(f"Coefficients de régression: {model.coef_}")
