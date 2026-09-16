# Jak main-1.py, ale z użyciem składni @CreateFunctionWithWrapper (prawdziwy dekorator).
import datetime


def CreateFunctionWithWrapper(func):
    def func_with_wrapper(*args, **kwargs):
        print(
            f'Function "{func.__name__}" started at {datetime.datetime.now().isoformat()}'
        )
        print("Following arguments were used:")
        print(args, kwargs)
        result = func(*args, **kwargs)
        print(f"Function returned {result}")
        return result

    return func_with_wrapper


@CreateFunctionWithWrapper
def ChangeSalary(emp_name, new_salary, is_bonus=False):
    print(f"Changing salary for {emp_name} to {new_salary} as bonus {is_bonus}")
    return new_salary


print(ChangeSalary("David", 40000, is_bonus=True))
# Function "ChangeSalary" started at 2024-12-01T19:38:57.745675
# Following arguments were used:
# ('David', 40000) {'is_bonus': True}
# Changing salary for David to 40000 as bonus True
# Function returned 40000
# 40000
