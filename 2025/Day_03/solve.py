import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)

def get_file_input(file:str | Path = 'inputfile.txt'):
    with Path(file).open("r") as f:
        for line in f:
            yield line.strip()

# === PARTIE 1 ===
jolts = get_file_input()
answer_pt1 = 0
for jolt_values in jolts:
    first_digit = max([int(l) for l in jolt_values[:-1]])
    first_digit_position = jolt_values.find(str(first_digit))
    second_digit = max(int(i) for i in jolt_values[first_digit_position+1:])
    logging.debug(f"{jolt_values} - {first_digit}{second_digit} ({first_digit_position})")
    answer_pt1 += int(f"{first_digit}{second_digit}")

logging.info(f"Maximum joltage : {answer_pt1}")