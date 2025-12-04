from aoc2025.utils import read_input
import numpy as np
from scipy.signal import convolve2d

# === PARTIE 1 ===
grid_txt = read_input()

# conversion des caractères en nombres
mapper={"@":1, ".":0}
data = [
    [mapper[c] for c in line]
    for line in grid_txt
]

grid = np.array(data)
kernel = np.array([
    [1,1,1],
    [1,0,1],
    [1,1,1]
])
# applique une convolution simple pour compter le nombre de voisin d'une cell
convo = convolve2d(grid, kernel, mode='same', boundary='fill')
# filtre la convo avec la valeur du centre
filter = np.where((grid==1) & (convo<4), 1, 0)
filter.sum()

print(f"Il y a {filter.sum()} rouleaux accessibles en forklift pour l'input donné.")