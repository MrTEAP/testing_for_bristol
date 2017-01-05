from fib import *

def test_fib_0():
    calculated_value_0 = fib(0)
    expected_value_0 = 1
    assert calculated_value_0 == expected_value_0, "something went wrong"

def test_fib_1():
    calculated_value_1 = fib(1)
    expected_value_1 = 1
    assert calculated_value_1 == expected_value_1, "something went wrong"

def test_fib_5():
    calculated_value_1 = fib(5)
    expected_value_1 = 8
    assert calculated_value_1 == expected_value_1, "something went wrong"
