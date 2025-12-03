import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)

def get_file_input(file:str | Path = 'inputfile.txt'):
    with Path(file).resolve().open("r") as f:
        for line in f:
            yield line.strip()

def find_max_joltage(jolt_values:str, jolt_len:int = 2, acc:list=None) -> int:
    if acc is None: acc = []
    logging.debug(f"début fonction : {jolt_values}, {jolt_len}, {acc}")
    # condition de fin : dernier chiffre à trouvé
    if jolt_len - 1 == 0:
        acc.append(str(max(int(i) for i in jolt_values)))
        # renvoie le nombre assemblé
        logging.debug(f"retour de fontion : {acc}")
        return int(''.join(acc))
    
    nth_digit = max(int(i) for i in jolt_values[:-(jolt_len-1)])
    nth_digit_position = jolt_values.find(str(nth_digit))
    acc.append(str(nth_digit))
    logging.debug(f"avant appel récursif : digit={nth_digit} - pos={nth_digit_position} - cumul={acc}")
    return find_max_joltage(jolt_values[nth_digit_position+1:], jolt_len - 1, acc)

# === PARTIE 1 ===
jolts = get_file_input()
answer_pt1 = 0

for jolt_values in jolts:
    logging.debug(f"{jolt_values}")
    res = find_max_joltage(jolt_values, 2)
    answer_pt1 += res
    if logging.getLogger().isEnabledFor(logging.DEBUG):
        flag = input("stop ?")
        if flag == 'y': break

logging.info(f"Maximum joltage : {answer_pt1}")

# === PARTIE 2 ===
jolts = get_file_input()
answer_pt2 = 0

for jolt_values in jolts:
    res = find_max_joltage(jolt_values, 12)
    answer_pt2 += res

logging.info(f"Maximum joltage OVERCHARGED : {answer_pt2}")