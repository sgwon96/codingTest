from itertools import permutations, combinations


def is_prime_number(x):
    if x <= 2:
        return False

    for y in range(2, x):
        if x % y == 0:
            return False

    return True


def solution(numbers):
    numbers = list(numbers)
    primes = set()
    for i in range(1, len(numbers) + 1):
        for nums in list(combinations(numbers, i)):
            for num in list(permutations(nums)):
                n = int(''.join(list(map(str, num))))
                if is_prime_number(n):
                    primes.add(n)

    return len(primes)