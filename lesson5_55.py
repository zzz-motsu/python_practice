def outer(a, b):

    def plus(c, d):
        return c + d

    r1 = plus(a, b)
    r2 = plus(a, b)
    print(r1 + r2)

outer(1, 2)
