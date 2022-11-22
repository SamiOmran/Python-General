import math
from heron_error import HeronError


def triangle_area(a, b, c):
    sides = sorted((a, b, c))
    if sides[2] > sides[0] + sides[1]:
        raise HeronError("Illegal triangle", sides)

    p = (a + b + c) / 2
    a = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return a


