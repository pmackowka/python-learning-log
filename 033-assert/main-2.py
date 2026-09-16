"""pytest to jedno z najbardziej popularnych narzędzi do testowania w Pythonie, używane do pisania i wykonywania testów:
- jednostkowych
- funkcjonalnych
- integracyjnych"""

# 1. Testy jednostkowe (Unit Tests)


def add(a, b):
    return a + b


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


test_add()

# 2. Testy funkcjonalne (Functional Tests)


# Plik: login.py
def login(username, password):
    if username == "admin" and password == "1234":
        return "Success"
    return "Failure"


def test_login_success():
    assert login("admin", "1234") == "Success"


def test_login_failure():
    assert login("user", "wrong") == "Failure"


test_login_success()
test_login_failure()

# 3. Testy integracyjne (Integration Tests)

# Plik: database.py
import sqlite3


def fetch_users():
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE users (id INTEGER, name TEXT)")
    conn.execute("INSERT INTO users VALUES (1, 'John'), (2, 'Jane')")
    cursor = conn.execute("SELECT name FROM users")
    return [row[0] for row in cursor]


# test_database.py
def test_fetch_users():
    users = fetch_users()
    assert users == ["John", "Jane"]
