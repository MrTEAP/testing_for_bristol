from mean import *

def test_ints():
    input = [1,2,3,4,5]
    calculated_value = mean(input)
    expected_value = 3
    assert calculated_value == expected_value, "Something went wrong. Uh oh."

def test_float():
    calculated_value = mean([1.0,2.0,3.0])
    expected_value = 2.0
    assert calculated_value == expected_value, "Something floaty"

#running py.test on the bash command line searches for all python scripts starting with "test". It then runs these scripts summing up functions that passed and failed.
