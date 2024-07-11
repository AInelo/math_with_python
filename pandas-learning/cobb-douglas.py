import pandas as pd 
data = {"company": ["Daimler", "E.ON", "Siemens", "BASF", "BMW"],
"price": [69.2, 8.11, 110.92, 87.28, 87.81],
"volume": [4456290, 3667975, 3669487, 1778058, 1824582]}
frame = pd.DataFrame(data)
print(frame)
print('--------------------O------------------------')
frameload = frame.describe() 
print(frameload)
# import numpy as np
# import matplotlib.pyplot as plt

# # Paramètres de la fonction d'utilité de Cobb-Douglas
# alpha = 0.6
# beta = 0.4

# # Définir les quantités de biens x et y
# x = np.linspace(0.1, 10, 100)  # Valeurs de x de 0.1 à 10
# y_utility = x**alpha * (10 - x)**beta  # Fonction d'utilité de Cobb-Douglas

# # Définir la courbe de demande du marché tangent à la fonction d'utilité
# x_demand = np.linspace(0.1, 10, 100)  # Valeurs de x pour la demande du marché
# y_demand = (alpha / beta) * (10 - x_demand)  # Courbe de demande tangent à la fonction d'utilité

# # Tracer les courbes
# plt.plot(x, y_utility, label='Fonction d\'utilité de Cobb-Douglas')
# plt.plot(x_demand, y_demand, label='Courbe de demande du marché', linestyle='--')

# # Ajouter des annotations
# plt.title("Fonction d'utilité de Cobb-Douglas et courbe de demande du marché")
# plt.xlabel("Quantité de bien x")
# plt.ylabel("Utilité / Demande")
# plt.legend()

# # Afficher le graphique
# plt.grid(True)
# plt.show()
