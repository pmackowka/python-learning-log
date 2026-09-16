# Lista funkcji (placeholderów) wywoływanych po kolei w pętli - prosty sterownik komend.
def GoLeft(*args):
    print("PLACEHOLDER - TURNING left with", *args)


def GoRight(*args):
    print("PLACEHOLDER - TURNING right with", *args)


def MoveForward(*args):
    print("PLACEHOLDER - MOVING forward with", *args)


def MoveBackward(*args):
    print("PLACEHOLDER - MOVING backward with", *args)


def Stop(*args):
    print("PLACEHOLDER - STOPPING with", *args)


def Start(*args):
    print("PLACEHOLDER - START with", *args)


instructions = [Start, GoLeft, MoveForward, Stop]

dish = "pizza"
for inst in instructions:
    inst(dish)  # Start('pizza')
