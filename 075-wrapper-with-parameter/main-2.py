"""Jak main-1.py, ale dekorator przyjmuje parametr - ścieżkę pliku logu (dekorator z argumentem)."""

import datetime
from pathlib import Path


def CreateFunctionWithWrapper_LogToFile(logFilePath):
    def CreateFunctionWithWrapper(func):
        def func_with_wrapper(*args, **kwargs):
            file = open(logFilePath, "a")
            file.write("-" * 20 + "\n")
            file.write(
                f'Function "{func.__name__}" started at {datetime.datetime.now().isoformat()}\n'
            )
            file.write("Following arguments were used:\n")
            file.write(
                " ".join(f"{i}" for i in args)
            )  # Zapisywać mogę tylko str więc konwertuje
            file.write("\n")
            file.write(" ".join(f"{k}={v}\n" for k, v in kwargs.items()))
            result = func(*args, **kwargs)
            file.write(f"Function returned {result}\n")
            file.close()
            return result

        return func_with_wrapper

    return CreateFunctionWithWrapper


@CreateFunctionWithWrapper_LogToFile(Path(__file__).parent / "salary_log.txt")
def ChangeSalary(emp_name, new_salary, is_bonus=False):
    print(f"Changing salary for {emp_name} to {new_salary} as bonus {is_bonus}")
    return new_salary


@CreateFunctionWithWrapper_LogToFile(Path(__file__).parent / "position_log.txt")
def ChangePosition(emp_name, new_position):
    print(f"Changing position for {emp_name} to {new_position}")
    return new_position


print(ChangeSalary("David", 40000, is_bonus=True))
print(ChangeSalary("David", 40000, False))

print(ChangePosition("Fox", "Policeman"))
print(ChangePosition("Megan", "Manager"))


# --------------------
# Function "ChangePosition" started at 2024-12-02T13:58:54.865862
# Following arguments were used:
# Fox Policeman
# Function returned Policeman
# --------------------
# Function "ChangePosition" started at 2024-12-02T13:58:54.865907
# Following arguments were used:
# Megan Manager
# Function returned Manager

# --------------------
# Function "ChangeSalary" started at 2024-12-02T13:58:54.865691
# Following arguments were used:
# David 40000
# is_bonus=True
# Function returned 40000
# --------------------
# Function "ChangeSalary" started at 2024-12-02T13:58:54.865789
# Following arguments were used:
# David 40000 False
# Function returned 40000
