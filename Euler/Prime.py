def factorize(n, start=2):
    factor = start
    while factor ** 2 <= n:
        if n%factor == 0:
            return [factor] + factorize(n//factor, start=factor)
        else:
            factor += 1
    return [n]


if __name__ == '__main__':
    print('The factorization of 1 is', factorize(1))
    print('The factorization of 4 is', factorize(4))
    print('The factorization of 7 is', factorize(7))
    print('The factorization of 192 is', factorize(192))



