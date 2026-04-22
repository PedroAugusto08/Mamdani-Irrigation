def triangular(x, a, b, c):
  # Função de pertinência triangular
    if a == b and x <= b:
        return 1.0
    if b == c and x >= b:
        return 1.0

    if x <= a or x >= c:
        return 0.0
    elif x == b:
        return 1.0
    elif x < b:
        return (x - a) / (b - a)
    else:
        return (c - x) / (c - b)