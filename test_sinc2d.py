from sinc2d import *

def test_xy0():
    inputX = 0.0
    inputY = 0.0
    calculated_value = sinc2d(inputX, inputY)
    expected_value = 1
    assert calculated_value == expected_value, "Something went wrong. Uh oh."

def test_x0():
    inputX = 0.0
    inputY = 1 #can be anything
    calculated_value = sinc2d(inputX, inputY)
    expected_value = np.sin(inputY) / inputY
    assert calculated_value == expected_value, "Something went wrong. Uh oh."

def test_y0():
    inputX = 1 #can be anything
    inputY = 0.0
    calculated_value = sinc2d(inputX, inputY)
    expected_value = np.sin(inputX) / inputX
    assert calculated_value == expected_value, "Something went wrong. Uh oh."

def test_xy():
    inputX = 5 #can be anything
    inputY = 5 #can be anything
    calculated_value = sinc2d(inputX, inputY)
    expected_value = (np.sin(inputX) / inputX) * (np.sin(inputY) / inputY)
    assert calculated_value == expected_value, "Something went wrong. Uh oh."
