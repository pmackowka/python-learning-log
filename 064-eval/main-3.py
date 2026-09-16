# eval() z pustym globals() nadal pozwala na __import__ - pokazuje, że samo
# ograniczenie globals nie wystarcza, żeby bezpiecznie odizolować eval().
var_x = 10
password = "jhjchwcFRWfw434"
source = '__import__("os").getcwd()'  # Fragment kodu od użytkownika
# source = 'password'  # Fragment kodu od użytkownika

globals = {}

print("-" * 20)

# Wykonanie kodu z eval
result = eval(source, globals)
print(result)  # Oczekiwany wynik: ścieżka bieżącego katalogu roboczego
