# Powtórzenie main-3.py - funkcja zwracająca True/False dla poprawności argumentu.
def PrintAnimal(animal=""):
    # this function prints a cat, bear or bat ascii-art
    txt_cat = r"""
|\---/|
| o_o |
 \_^_/"""
    txt_bear = r'''
/  \.-"""-./  \
\    -   -    /
 |   o   o   |
 \  .-'"'-.  /
  '-\__Y__/-'
     `---`'''
    txt_bat = r"""
   /\                 /\
  / \'._   (\_/)   _.'/ \
 /_.''._'--('.')--'_.''._\
 | \_ / `;=/ " \=;` \ _/ |
  \/ `\__|`\___/`|__/`  \/
          \(/|\)/
     """

    if animal == "cat":
        print(txt_cat)
    elif animal == "bear":
        print(txt_bear)
    elif animal == "bat":
        print(txt_bat)
    else:
        print(
            "Cannot print '%s'. Correct values for the parameter are: cat, bear, bat"
            % animal
        )
        return False

    return True


if PrintAnimal():
    print("The parameter was correct")
else:
    print("The parameter was INCORRECT")


if PrintAnimal("dog"):
    print("The parameter was correct")
else:
    print("The parameter was INCORRECT")


if PrintAnimal("bat"):
    print("The parameter was correct")
else:
    print("The parameter was INCORRECT")
