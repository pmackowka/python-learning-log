"""Ćwiczenie funkcji os.listdir, os.path.join i os.path.isdir na przykładowym katalogu."""

import os
from pathlib import Path

sample_dir = Path(__file__).parent / "sample_dir"

print("-" * 30)
print(os.listdir(sample_dir))
# ['b.txt', 'a.txt', 'nested']

print("-" * 30)
print(os.path.join(sample_dir, "a.txt"))
# .../sample_dir/a.txt

print("-" * 30)
print(os.path.isdir(sample_dir))
# True
