# Funkcje jako elementy listy (przepis kulinarny jako para funkcja+argument), wywoływane w pętli.
def Bake(what):
    print(f"Baking {what}")


def Add(what):
    print(f"Adding {what}")


def Mix(what):
    print(f"Mixing {what}")


cookbook = [
    (Add, "milk"),
    (Add, "eggs"),
    (Add, "flour"),
    (Add, "sugar"),
    (Mix, "ingredients"),
    (Bake, "cookies"),
]

for activity, obj in cookbook:
    activity(obj)

# Adding milk
# Adding eggs
# Adding flour
# Adding sugar
# Mixing ingredients
# Baking cookies

print("-" * 30)


def Cook(activity, obj):
    activity(obj)


Cook(Bake, "kawa")
# Baking kawa

print("-" * 30)

for activity, obj in cookbook:
    Cook(activity, obj)

# Adding milk
# Adding eggs
# Adding flour
# Adding sugar
# Mixing ingredients
# Baking cookies
