import logging
from pathlib import Path
from collections import Counter


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
dial = 50

def get_dial_changes(filepath:str | Path):
    """Ouvre le fichier d'input et crée un générateur qui renvoie chaque ligne à chaque itération

    Parameters
    ----------
    filepath : str | Path
        chemin du fichier d'input AoC

    Yields
    ------
    Tuple[int, int]
        Entier indiquant si la somme est à ajouter ou retrancher
        Valeur à ajouter

    Raises
    ------
    ValueError
        Si le fichier n'existe pas
    """
    filepath = Path(filepath)
    if not filepath.exists():
        logging.critical(f"Le chemin `{filepath}` n'existe pas !")
        raise ValueError(f"Chemin incorrect. Interruption.")
    
    with Path(filepath).open("r") as f:
        for line in f:
            direction = -1 if line[0] == 'L' else 1 # else = line[0] == 'R'
            try:
                value = int(line[1:])
            except ValueError as ve:
                logging.error(f"{line[1:]} n'est pas un nombre ; {ve}")
            except Exception as e:
                logging.critical(f"Innatendu : {e}")
            
            yield direction, value

# === PARTIE 1 ===
logging.info(f"Partie 1 - Dial : {dial}")

def part_1(dial_start = 50):
    """Isole la logique de la partie 1. 
    Compte le nombre de fois où un mouvement se termine sur la valeur 0."""
    values = Counter()
    dial = dial_start

    # init du générateur qui lit chaque ligne du fichier
    lines = get_dial_changes('inputfile.txt')

    for dir, val in lines:
        change = dir * val
        logging.debug(f"value : {val}, direction : {dir}, product : {change}")

        dial += change
        logging.debug(f"dial + change : {dial}")
        dial %= 100
        logging.debug(f"dial mod 100 : {dial}")
        values[dial] += 1
    return values[0]

part_1_code = part_1()
logging.info(f"nombre de fois où le coffre affiche zéro : {part_1_code}")

# === PARTIE 2 ===
logging.info(f"Partie 2 :")
values = Counter()
lines_part_2 = get_dial_changes('inputfile.txt')
for dir, val in lines_part_2:
    # debug helper
    logging.debug(f"==== Nouvelle étape ====")
    logging.debug(f"direction : {dir}, value : {val}")
    if logging._Level == logging.DEBUG:
        flag = input("stop ?")
        if flag == 'y': break

    # approche "brute", itère chaque "clic" du coffre et enregistre le numéro visité
    for i in range(val):
        logging.debug(f"dial before step: {dial}, direction {dir}, step {i}")
        # ajoute (ou retire) 1
        dial += dir
        # recadre dans le range 0-100
        dial %= 100
        # incrémente le compteur de visites
        values[dial] += 1
        logging.debug(f"dial after step: {dial}, direction {dir}, step {i}")

logging.info(f"Nombre de fois où le pointeur passe par zéro : {values[0]}")
