from mymodule.math import add, sub

def test_add():
    assert add(2, 3) == 5

def test_sub():
    assert sub(3, 3) == 0

def test_sub2():
    assert sub(5, 3) == 2
