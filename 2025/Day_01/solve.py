import logging
from pathlib import Path
from collections import Counter


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
dial = 50
values = Counter()

def get_dial_changes(filepath:str | Path):
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


logging.info(f"Partie 1 - Dial : {dial}")
def part_1(dial_start = 50):
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
logging.info(f"Partie 2 :")
values.clear()
lines_part_2 = get_dial_changes('inputfile.txt')
for dir, val in lines_part_2:
    logging.debug(f"==== Nouvelle étape ====")
    logging.debug(f"direction : {dir}, value : {val}")
    for i in range(val):
        logging.debug(f"dial before step: {dial}, direction {dir}, step {i}")
        dial += dir
        dial %= 100
        values[dial] += 1
        logging.debug(f"dial after step: {dial}, direction {dir}, step {i}")
    # flag = input("stop ?")
    # if flag == 'y': break

logging.info(f"Nombre de fois où le pointeur passe par zéro : {values[0]}")
