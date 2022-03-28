import Divisible
import pytest

def testdivisibleby5():
    x = 10
    result = Divisible.divisibleby5(x)
    assert result == True


def testdivisibleby7():
    x = 11
    result = Divisible.divisibleby7(x)
    assert result == True


def testdivisibleby9():
    x = 18
    result = Divisible.divisibleby9(x)
    assert result == True


def testdivisibleby10():
    x = 19
    result = Divisible.divisibleby10(x)
    assert result == True

