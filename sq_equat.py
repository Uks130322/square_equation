def sq_equat(a: float, b: float, c: float) -> list:
    """
    Solve the square equation
    ax**2 + bx + c = 0
    round to two signs

    """
    
    if a == b == c == 0:
        return ["Any number is a root"]
    
    d = discriminant(a, b, c)
    if d < 0:
        return ["No roots"]
    elif d == 0:
        return [round(-b / (2 * a), 2)]
    else:
        return [round((-b - d * 0.5) / (2 * a), 2),
                round((-b + d * 0.5) / (2 * a), 2)]


def discriminant(a: float, b: float, c: float) -> float:
    """
    Find the discriminant of the square equation
    ax**2 + bx + c = 0
    no round

    """

    return b ** 2 - 4 * a * c
