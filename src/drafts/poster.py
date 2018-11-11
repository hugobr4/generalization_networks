from scipy.stats import norm
import numpy as np
from matplotlib import pyplot as plt


# p stands for 'proximity'
# ranging from 0.0, to 1.0, and back to 0.0
p1 = np.linspace(0.0, 1.0, 40)
p2 = np.linspace(1.0, 0.0, 40)
p = np.insert(p2, 0, values=p1)

# difference between the colors
delta = list(range(-40, 40))

# Botar isso na distribuição normal
dist = list(zip(l3, delta))
