def euclid_gcd(a, b):
    if a == b:
        return a
    elif a > b:
        a -= b
        return euclid_gcd(a, b)
    elif a < b:
        b -= a
        return euclid_gcd(a, b)
