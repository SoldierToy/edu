import pytest
from codewars.count_the_divisors_of_number import divisors


@pytest.mark.parametrize('num, res', [
    (474525, 48),
    (1936, 15),
    (439848, 48),
    (444833, 2)
])
def test_divisor(num, res):
    assert divisors(num) == res
