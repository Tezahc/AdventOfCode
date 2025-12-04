from aoc2025.utils import read_input
import numpy as np
# from scipy.signal import convolve2d
import cv2

grid_txt = read_input()

# conversion des caractères en nombres
mapper={"@":1, ".":0}
data = [
    [mapper[c] for c in line]
    for line in grid_txt
]
grid_ini = np.array(data, np.uint8)

kernel = np.array([
    [1,1,1],
    [1,0,1],
    [1,1,1]
], np.uint8)

def get_accessible_rolls(grid: np.ndarray, kernel:np.ndarray) -> np.ndarray:
    centers = grid.copy()
    
    # applique une convolution simple pour compter le nombre de voisin d'une cellule
    # neighbours = convolve2d(centers, kernel, mode="same", boundary="fill")
    neighbours = cv2.filter2D(grid, -1, kernel, borderType=cv2.BORDER_CONSTANT)
    # filtre la convo avec la valeur du centre
    reachables = np.where((centers==1) & (neighbours<4), 1, 0)
    
    return reachables

# === PARTIE 1 ===
answer_pt1 = get_accessible_rolls(grid_ini, kernel).sum()
print(f"Il y a {answer_pt1} rouleaux accessibles en forklift pour l'input donné.")
