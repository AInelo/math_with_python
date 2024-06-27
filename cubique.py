import numpy as np
import matplotlib.pyplot as plt

def spline_cubique(x, y):
    n = len(x) - 1  # nombre d'intervalles
    
    # Étape 1: Calcul des h
    h = np.diff(x)
    
    # Étape 2: Calcul des alpha
    alpha = [0] * (n+1)
    for i in range(1, n):
        alpha[i] = (3/h[i]) * (y[i+1] - y[i]) - (3/h[i-1]) * (y[i] - y[i-1])
    
    # Étape 3: Résolution du système tridiagonal
    l = [1] + [0] * n
    mu = [0] * (n+1)
    z = [0] * (n+1)
    
    for i in range(1, n):
        l[i] = 2 * (x[i+1] - x[i-1]) - h[i-1] * mu[i-1]
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i-1] * z[i-1]) / l[i]
    
    l[n] = 1
    z[n] = 0
    
    # Étape 4: Calcul des coefficients c, b, et d
    c = [0] * (n+1)
    b = [0] * n
    d = [0] * n
    
    for j in range(n-1, -1, -1):
        c[j] = z[j] - mu[j] * c[j+1]
        b[j] = (y[j+1] - y[j]) / h[j] - h[j] * (c[j+1] + 2*c[j]) / 3
        d[j] = (c[j+1] - c[j]) / (3 * h[j])
    
    # Stocker les coefficients a (qui sont les y)
    a = y[:-1]
    
    # Retourner les coefficients des polynômes de la spline
    return a, b, c[:-1], d

def eval_spline(x, coeffs, x_new):
    a, b, c, d = coeffs
    y_new = []
    
    for x_i in x_new:
        # Trouver l'intervalle correct pour x_i
        for i in range(len(x)-1):
            if x[i] <= x_i <= x[i+1]:
                dx = x_i - x[i]
                y_i = a[i] + b[i] * dx + c[i] * dx**2 + d[i] * dx**3
                y_new.append(y_i)
                break
                
    return np.array(y_new)

# Exemple de données
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 1, 0, 1, 0, 1])

# Calcul des coefficients de la spline cubique
coeffs = spline_cubique(x, y)

# Points pour évaluer la spline
x_new = np.linspace(x.min(), x.max(), 100)
y_new = eval_spline(x, coeffs, x_new)

# Visualisation
plt.plot(x, y, 'o', label='Données originales')
plt.plot(x_new, y_new, label='Spline cubique')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interpolation par spline cubique (implémentation personnalisée)')
plt.show()
