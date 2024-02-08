import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Paramètres
A = 0.100  # N
m = 0.100  # kg
omega = np.pi / 3.00  # rad/s

# Symboles
t = sp.symbols('t')

# Expression de vx
vx_expression = A * (-omega * t * sp.cos(omega * t) + sp.sin(omega * t)) / (m * omega**2)

# Fonction de vx en fonction de t
vx_fonction = sp.lambdify(t, vx_expression, 'numpy')

# Générer des valeurs de t
t_valeur = np.linspace(0, 6.00, 100)

# Calculer vx pour les valeurs de t
vx_valeur = vx_fonction(t_valeur)

# Tracer le graphe de vx en fonction de t
plt.plot(t_valeur, vx_valeur)
plt.title("Vitesse en fonction du temps")
plt.xlabel("Temps (s)")
plt.ylabel("Vitesse vx (m/s)")
plt.grid(True)
plt.show()
