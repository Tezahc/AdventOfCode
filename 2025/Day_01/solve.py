import logging
from pathlib import Path
from collections import Counter


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
dial = 50
logging.info(f"Dial : {dial}")
values = Counter()

with Path("./inputfile.txt").open("r") as f:
    for line in f:
        direction = -1 if line[0] == 'L' else 1
        try:
            value = int(line[1:])
        except ValueError as ve:
            logging.error(f"{line[1:]} n'est pas un nombre ; {ve}")
        except Exception as e:
            logging.critical(f"Innatendu : {e}")

        change = direction * value
        logging.debug(f"value : {value}, direction : {direction}, product : {change}")

        dial += change
        logging.debug(f"dial + change : {dial}")
        dial %= 100
        logging.debug(f"dial mod 100 : {dial}")
        values[dial] += 1

logging.info(f"nombre de fois où le coffre affiche zéro : {values[0]}")