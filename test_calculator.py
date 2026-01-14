import pytest

def test_multiply():
    from calculator import multiply
    assert multiply(6, 2) == 12, "Expected 6 * 2 to be 12"
    assert multiply(0, 5) == 0, "Expected 0 * 5 to be 0"
    assert multiply(-2, 6) == -12, "Expected -2 * 6 to be -12"

def test_add():
    from calculator import add
    assert add(6, 2) == 8, "Expected 6 + 2 to be 8"
    assert add(-5, 5) == 0, "Expected -5 + 5 to be 0"
    assert add(0, 0) == 0, "Expected 0 + 0 to be 0"

def test_subtract():
    from calculator import subtract
    assert subtract(6, 2) == 4, "Expected 6 - 2 to be 4"
    assert subtract(0, 5) == -5, "Expected 0 - 5 to be -5"
    assert subtract(-3, -7) == 4, "Expected -3 - (-7) to be 4"

def test_divide():
    from calculator import divide
    assert divide(6, 2) == 3, "Expected 6 / 2 to be 3"
    assert divide(-9, 3) == -3, "Expected -9 / 3 to be -3"
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)  # Ensure it raises an exception for divide by zero

def test_square():
    from calculator import square
    assert square(6) == 36, "Expected 6^2 to be 36"
    assert square(2) == 4, "Expected 2^2 to be 4"
    assert square(-2) == 4, "Expected (-2)^2 to be 4"

def test_cube():
    from calculator import cube
    assert cube(6) == 216, "Expected 6^3 to be 216"
    assert cube(2) == 8, "Expected 2^3 to be 8"
    assert cube(-2) == -8, "Expected (-2)^3 to be -8"
