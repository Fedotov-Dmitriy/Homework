def evklidalg(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = evklidalg(b, a % b)
        return d, y, x - y * (a // b)
