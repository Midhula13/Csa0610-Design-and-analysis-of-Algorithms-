def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = n // 2

    a = x // (10 ** m)
    b = x % (10 ** m)

    c = y // (10 ** m)
    d = y % (10 ** m)

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    abcd = karatsuba(a + b, c + d)

    return ac * (10 ** (2 * m)) + (abcd - ac - bd) * (10 ** m) + bd


x = int(input())
y = int(input())

print(karatsuba(x, y))
