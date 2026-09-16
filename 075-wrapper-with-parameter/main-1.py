"""Dekorator logujący wywołania funkcji (argumenty, wynik, timestamp) do pliku function_log.txt."""

import datetime
from pathlib import Path

function_log = Path(__file__).parent / "function_log.txt"


def CreateFunctionWithWrapper(func):
    def func_with_wrapper(*args, **kwargs):
        file = open(function_log, "a")
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


@CreateFunctionWithWrapper
def ChangeSalary(emp_name, new_salary, is_bonus=False):
    print(f"Changing salary for {emp_name} to {new_salary} as bonus {is_bonus}")
    return new_salary


print(ChangeSalary("David", 40000, is_bonus=True))
print(ChangeSalary("David", 40000, False))


# --------------------
# Function "ChangeSalary" started at 2024-12-02T12:35:50.758219
# Following arguments were used:
# David 40000
# is_bonus=True
# Function returned 40000
# --------------------
# Function "ChangeSalary" started at 2024-12-02T12:35:50.758340
# Following arguments were used:
# David 40000 False
# Function returned 40000
