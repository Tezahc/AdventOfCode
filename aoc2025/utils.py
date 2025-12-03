import inspect
from pathlib import Path
from typing import Any, Generator

def read_input(file:str | Path = 'inputfile.txt') -> Generator[str, Any, None]:
    # récupère le path du fichier appelant la fonction
    caller_file = Path(inspect.stack()[1].filename).resolve().parent
    filepath = caller_file / file

    with Path(filepath).open("r") as f:
        for line in f:
            yield line.strip()