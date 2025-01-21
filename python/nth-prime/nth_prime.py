def prime(number):
    if number < 1:
        raise ValueError("there is no zeroth prime")
    primes = eratosthenes_sieve()
    for n in range(number):
        nth_prime = next(primes)
    return nth_prime


# Sieve of Eratosthenes
# David Eppstein, UC Irvine, 28 Feb 2002
def eratosthenes_sieve():
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1
