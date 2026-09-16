"""LAB - Funkcja exec() (wariant main-2.py bez os.path.basename w print)."""

import os
from pathlib import Path

BASE_DIR = Path(__file__).parent
files_to_process = [
    BASE_DIR / "main-3.py",
    BASE_DIR / "main-4.py",
]

for file_path in files_to_process:
    with open(file_path, "r") as f:
        print(f"File {os.path.basename(file_path)} ...")
        source = f.read()
        exec(source)
