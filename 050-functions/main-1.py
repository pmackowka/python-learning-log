# Funkcja z parametrem bez wartości domyślnej vs. z wartością domyślną - ASCII-art zwierząt.
def PrintAnimal(animal):
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


# PrintAnimal('cat')
# PrintAnimal(animal='bear')
PrintAnimal(animal="bat")
PrintAnimal("unicorn")


print("----------------")


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
