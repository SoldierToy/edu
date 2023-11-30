import pytest


def divisors(n):
    cnt = 0

    for num in range(1, n + 1):
        if n % num == 0:
            cnt += 1

    return cnt


print(divisors(10))


