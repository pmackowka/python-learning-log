"""Zapis dowolnych danych przekazanych jako **kwargs do pliku tekstowego."""

import tempfile
from pathlib import Path


def save_user_data(**kwargs):
    data = kwargs
    print("User data:", data)

    user_data = Path(tempfile.gettempdir()) / "user_data.txt"

    with open(user_data, mode="a", encoding="utf-8") as file:
        file.writelines(f"{key}: {value}\n" for key, value in data.items())
        file.write("\n")


save_user_data(name="John Doe", age=30, occupation="Engineer", city="New York")
save_user_data(name="Jane Smith", age=25, occupation="Designer", city="Los Angeles")
