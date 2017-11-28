def factorize(n, start=2):
    factor = start
    while factor ** 2 <= n:
        if n%factor == 0:
            return [factor] + factorize(n//factor, start=factor)
        else:
            factor += 1
    return [n]


def prime_under(n):
    remain = list(range(2, n))
    save = []
    key = min(remain)
    while key**2 <= n:
        remain = list(filter(lambda x: x % key, remain))
        save.append(key)
        key = min(remain)
    return save + remain


if __name__ == '__main__':
    print('The factorization of 1 is', factorize(1))
    print('The factorization of 192 is', factorize(192))
    print('Primes under 20 are', prime_under(20))



