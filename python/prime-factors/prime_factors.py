def factors(value):
    if value == 1:
        return []
    ret_val = []
    for prime in eratosthenes_sieve():
        while not value % prime:
            ret_val.append(prime)
            if (value := value // prime) == 1:
                return ret_val


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
