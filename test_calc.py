from calculatrice import addition, soustraction, multiplication, division

def test_addition():
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0
    assert addition(0, 0) == 0

def test_soustraction():
    assert soustraction(5, 3) == 2
    assert soustraction(0, 5) == -5

def test_multiplication():
    assert multiplication(2, 4) == 8
    assert multiplication(0, 10) == 0

def test_division():
    assert division(10, 2) == 5
    assert division(9, 3) == 3
