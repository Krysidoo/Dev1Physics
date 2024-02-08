import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Paramètres
A = 0.100  # N
m = 0.100  # kg
omega = np.pi / 3.00  # rad/s

# Symboles
t = sp.symbols('t')

# Expression de x
x_expression = A * (-omega * t * sp.sin(omega * t) - 2 * sp.cos(omega * t) + 2) / (m * omega**3)

# Fonction de x en fonction de t
x_fonction = sp.lambdify(t, x_expression, 'numpy')

# Générer des valeurs de t
t_valeur = np.linspace(0, 6.00, 100)

# Calculer x pour les valeurs de t
x_valeur = x_fonction(t_valeur)

# Tracer le graphe de x en fonction de t
plt.plot(t_valeur, x_valeur)
plt.title("Position en fonction du temps")
plt.xlabel("Temps (s)")
plt.ylabel("Position (m)")
plt.grid(True)
plt.show()
