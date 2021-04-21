from random import randint


def dice(code: str):
    dices = [3, 4, 6, 8, 10, 12, 20, 100]
    try:
        x = int(code[: code.index("D")])
        y = int(code[code.index("D") + 1: code.index("+")])
        z = int(code[code.index("+") + 1:])
    except ValueError as ve:
        print(ve)
        return None
    if not y in dices:
        print("There is no such dice!")
        return None
    result = 0
    for i in range(x):
        result += randint(1, y)
    return result + z


throw = dice("3D6+1")
print(throw)
