r"""LAB - Funkcja wrappera z parametrem
Pracujesz nad aplikacją, która intensywnie pracuje z plikami. Klient zażyczył sobie, aby każda taka operacja została dodatkowo zalogowana. Log powinien mieć postać mniej więcej taką:

Action FILE_CREATE executed on c:\temp\dummy_file.txt on 2029-01-12 9:29:17
Action FILE_DELETE executed on c:\temp\dummy_file.txt on 2029-01-12 9:33:18
Action FILE_CREATE executed on c:\temp\dummy_file.txt on 2029-01-12 9:39:57
Action FILE_DELETE executed on c:\temp\dummy_file.txt on 2029-01-12 9:44:18

Wiadomo, że:

wszystkie te funkcje przyjmują jeden parametr path (więc mogą korzystać z takiego samego wrappera)
klient może chcieć zapisać dane logowania oddzielnie do innego pliku dla każdej funkcji (więc wrappery jednak czymś będą się nieznacznie różnić)
Chcesz rozwiązać problem stosując wrapper. Idealnie będzie napisać jedną funkcję  przyjmującą jako parametry:
logged_action określającą wykonywaną czynność np. FILE_CREATE lub FILE_DELETE
log_file_path określającą do jakiego pliku zapisywać informacje
Oto przykład funkcji, których praca ma podlegać logowaniu:"""

import functools
import os
from datetime import datetime as dt
from pathlib import Path

BASE_DIR = Path(__file__).parent


def wrapper_with_log_file(logged_action, log_file_path):
    def wrapper_with_log_to_known_file(func):
        @functools.wraps(func)  # Zachowuje metadane dekorowanej funkcji
        def the_real_wrapper(path):
            with open(log_file_path, "a") as log_file:
                log_entry = f"Action {logged_action} executed on {path} on {dt.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                log_file.write(log_entry)
            return func(path)

        return the_real_wrapper

    return wrapper_with_log_to_known_file


@wrapper_with_log_file("FILE_CREATE", BASE_DIR / "file_create.txt")
def create_file(path):
    print(f"creating file {path}")
    open(path, "w+").close()


@wrapper_with_log_file("FILE_DELETE", BASE_DIR / "file_delete.txt")
def delete_file(path):
    print(f"deleting file {path}")
    os.remove(path)


# Testowanie funkcji
file_path = BASE_DIR / "dummy_file.txt"

create_file(file_path)  # Tworzenie pliku
delete_file(file_path)  # Usuwanie pliku
create_file(file_path)  # Ponowne tworzenie pliku
delete_file(file_path)  # Ponowne usuwanie pliku


# creating file .../075-wrapper-with-parameter/dummy_file.txt
# deleting file .../075-wrapper-with-parameter/dummy_file.txt
# creating file .../075-wrapper-with-parameter/dummy_file.txt
# deleting file .../075-wrapper-with-parameter/dummy_file.txt

# Action FILE_CREATE executed on .../dummy_file.txt on 2024-12-02 14:26:56
# Action FILE_CREATE executed on .../dummy_file.txt on 2024-12-02 14:26:56

# Action FILE_DELETE executed on .../dummy_file.txt on 2024-12-02 14:26:56
# Action FILE_DELETE executed on .../dummy_file.txt on 2024-12-02 14:26:56
