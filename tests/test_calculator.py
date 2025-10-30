from src.calculator import add, divide
import pytest

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

def test_will_fail():
    assert 1 == 3

def test_will_also_fail():
    assert 2 == 3

def phoenix_will_not_fail():
    assert "Phat. Faatt. Fat."[-4:] == "Fat."