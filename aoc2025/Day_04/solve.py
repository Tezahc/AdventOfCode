import logging
from aoc2025.utils import read_input
import numpy as np
from scipy.signal import convolve2d, convolve
# import cv2

logging.basicConfig(level=logging.INFO)
grid_txt = read_input()

# conversion des caractères en nombres
mapper={"@":1, ".":0}
data = [
    [mapper[c] for c in line]
    for line in grid_txt
]
grid_ini = np.array(data)

kernel = np.array([
    [1,1,1],
    [1,0,1],
    [1,1,1]
])

def get_accessible_rolls(grid: np.ndarray, kernel:np.ndarray) -> np.ndarray:
    # applique une convolution simple pour compter le nombre de voisin d'une cellule
    voisins = convolve2d(grid, kernel, mode="same", boundary="fill")
    # filtre la convo avec la valeur du centre
    return ((grid == 1) & (voisins < 4)).astype(np.int8)

# === PARTIE 1 ===
answer_pt1 = get_accessible_rolls(grid_ini, kernel).sum()
print(f"Il y a {answer_pt1} rouleaux accessibles en forklift pour l'input donné.")

# === PARTIE 2 ===
answer_pt2, i = 0, 0
grid = grid_ini.copy()
while True:
    # récupère les emplacements des rouleaux accessibles
    accessibles = get_accessible_rolls(grid, kernel)
    removed = accessibles.sum()

    if removed == 0:
        break

    logging.debug(f"{removed} Rouleaux trouvés à l'étape {i}")
    i+=1

    # met à jour le total
    answer_pt2 += removed
    # update la grille en retirant les rouleaux
    grid -= accessibles

print(f"L'ensemble des rouleaux accessibles avant d'être bloqué est de {answer_pt2}")