# Funkcja zwracająca inną funkcję - najpierw zwykła funkcja, potem funkcja
# generowana dynamicznie przez exec() na podstawie stringa.
def calculate(kind="+", *args):
    result = 0
    if kind == "+":
        for a in args:
            result += a
    elif kind == "-":
        for a in args:
            result -= a
    return result


print(calculate("+", 1, 2, 3))
print(calculate("-", 1, 2, 3))
# 6
# -6

print("-" * 30)


def create_functions(kind="+"):
    source = f"""
def f(*args):
	result = 0
	for a in args:
		result {kind}= a
	return result
"""
    exec(source, globals())

    return f


f_add = create_functions("+")
print(f_add(1, 2, 3))
f_subs = create_functions("-")
print(f_subs(1, 2, 3))
# 6
# -6
