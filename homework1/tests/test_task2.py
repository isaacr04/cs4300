from homework1.src.task2 import demonstrateVariables

def test_demonstrateVariables():
    types = demonstrateVariables()

    assert types[0] is int
    assert types[1] is float
    assert types[2]is str
    assert types[3] is bool