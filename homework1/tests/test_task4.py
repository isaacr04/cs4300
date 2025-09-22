from homework1.src.task4 import calculate_discount

def test_calculate_discount():
    assert calculate_discount(100, 20) == 80
    assert calculate_discount(100, 99.9) == 0.10
    assert calculate_discount(20.25, 10) == 18.23 # Should round up from 18.225 to 18.23
    assert calculate_discount(20.25, 10.5) == 18.12 # Should round down from 18.12375 to 18.12