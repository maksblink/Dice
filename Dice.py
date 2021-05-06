from random import randint


def dice(code: str):
    """Calculate dice roll from dice pattern.

    :param str code: dice pattern ex. `7D12-5`

    :rtype: str
    :dice roll value for proper dice pattern
    """
    dices = [3, 4, 6, 8, 10, 12, 20, 100]
    try:
        x = int(code[: code.index("D")])
        if "+" in code:
            y = int(code[code.index("D") + 1: code.index("+")])
            z = int(code[code.index("+") + 1:])
        else:
            y = int(code[code.index("D") + 1: code.index("-")])
            z = int(code[code.index("-") + 1:])
    except ValueError as ve:
        print(ve)
        return None
    if y not in dices:
        print("There is no such dice!")
        return None
    result = 0
    for i in range(x):
        result += randint(1, y)
    return result + z


throw = dice("1D12-5")
print(throw)
