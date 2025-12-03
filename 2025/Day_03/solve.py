import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)

def get_file_input(file:str | Path = 'inputfile.txt'):
    with Path(file).resolve().open("r") as f:
        for line in f:
            yield line.strip()

def digit_lookup(digits:str, start:int=None, end:int=None) -> str:
    digit = max(int(i) for i in digits[start:end])
    return str(digit)

def find_max_joltage(jolt_values:str, batt_len:int = 2, acc:list = None) -> int:
    if acc is None: acc = []
    logging.debug(f"début fonction : {jolt_values}, {batt_len}, {acc}")

    # condition de fin : dernier chiffre à trouvé
    if batt_len - 1 == 0:
        acc.append(digit_lookup(jolt_values))
        # renvoie le nombre assemblé
        logging.debug(f"retour de fontion : {acc}")

        return int(''.join(acc))
    
    nth_digit = digit_lookup(jolt_values, end=-(batt_len-1) )
    nth_digit_position = jolt_values.find(nth_digit)
    acc.append(nth_digit)
    logging.debug(f"avant appel récursif : digit={nth_digit} - pos={nth_digit_position} - cumul={acc}")

    return find_max_joltage(jolt_values[nth_digit_position+1:], batt_len-1, acc)


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