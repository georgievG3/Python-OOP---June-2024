def get_primes(numbers: list):

    for n in numbers:

        if n % 2 != 0 and n % 3 != 0 and n > 1 or n == 2 or n == 3:
            yield n


print(list(get_primes([223])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))

