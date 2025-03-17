def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    prime_numbers = [p for p in range(2, limit + 1) if is_prime[p]]
    return prime_numbers

testcase = int(input())

for _ in range(testcase):
    N = int(input())
    primes = sieve_of_eratosthenes(N)
    primes_dict = {i: 0 for i in primes}
    while N != 1:
        for i in primes:
            if N % i == 0:
                N = N // i
                primes_dict[i] += 1
                break
    for k, v in primes_dict.items():
        if v != 0:
            print(f"{k} {v}")
