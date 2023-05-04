def euclid(a, b):
    if a == b:
        return a
    elif a > b:
        a -= b
        return euclid(a, b)
    elif a < b:
        b -= a
        return euclid(a, b)
