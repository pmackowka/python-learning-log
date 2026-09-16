"""LAB - Funkcja partial
Oto funkcja pobierająca dane ze stron www:"""

import os
import tempfile

import requests


def save_url_file(url, dir, file, msg):

    print(msg.format(file))

    r = requests.get(url, stream=True)
    file_path = os.path.join(dir, file)

    with open(file_path, "wb") as f:
        f.write(r.content)


# Można ją wywołać korzystając z następującego kodu:

msg = "Please wait - the file {} will be downloaded"

url = "http://mobilo24.eu/spis"
dir = tempfile.gettempdir()
file = "spis.html"
save_url_file(url, dir, file, msg)

url = "https://www.mobilo24.eu/wp-content/uploads/2015/11/Mobilo_logo_kolko_512-565b1626v1_site_icon.png"
dir = tempfile.gettempdir()
file = "logo.png"
save_url_file(url, dir, file, msg)

r"""Na potrzeby projektu, nad którym pracujesz katalog pobierania plików powinien zawsze być taki sam (np. przyjmijmy c:\temp), a komunikat wyświetlany na ekranie powinien być zawsze "Please wait: {}"

Napisz funkcję partial  save_url_to_dir   która będzie mogła być wywoływana jedynie z argumentami url i file"""
