from ..src.task3 import *

def test_checksign():
    assert check_sign(15) == 1
    assert check_sign(-253.52) == -1
    assert check_sign(0) == 0

def test_prime():
    assert get_ten_primes() == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def test_sum():
    assert sum_1_to_100() == 5050