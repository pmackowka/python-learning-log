"""Jak main-3.py, bez functools.wraps - druga wersja wrappera z parametrem."""

import os
from datetime import datetime as dt
from pathlib import Path

BASE_DIR = Path(__file__).parent


def wrapper_with_log_file(logged_action, log_file_path):
    def wrapper_with_log_to_known_file(func):
        def the_real_wrapper(path):
            with open(log_file_path, "a") as f:
                f.write(
                    "Action {} executed on {} on {}\n".format(
                        logged_action, path, dt.now().strftime("%Y-%m-%d %H:%M:%S")
                    )
                )
            return func(path)

        return the_real_wrapper

    return wrapper_with_log_to_known_file


@wrapper_with_log_file("FILE_CREATE", BASE_DIR / "file_create-2.txt")
def create_file(path):
    print(f"creating file {path}")
    open(path, "w+")


@wrapper_with_log_file("FILE_DELETE", BASE_DIR / "file_delete-2.txt")
def delete_file(path):
    print(f"deleting file {path}")
    os.remove(path)


file_path = BASE_DIR / "dummy_file.txt"

create_file(file_path)
delete_file(file_path)
create_file(file_path)
delete_file(file_path)
