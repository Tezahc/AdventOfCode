from pathlib import Path
import re

with Path("inputfile.txt").open("r") as f:
    data = f.read()

# ranges = [(int(s.split("-")[0]), int(s.split("-")[1])) for s in data.strip().split(",")]
pids = data.strip().split(",")
answer_p1, answer_p2 = 0, 0

for pid_range in pids:
    bounds = pid_range.split("-")
    lower, upper = int(bounds[0]), int(bounds[1])
    for i in range(lower, upper+1):
        if re.match(r"^(.+)\1$", str(i)):
            answer_p1 += i
        if re.match(r"^(.+)\1+$", str(i)):
            answer_p2 += i
print(f"Total des id invalides : {answer_p1}")
print(f"Total de TOUS les id invalides : {answer_p2}")
