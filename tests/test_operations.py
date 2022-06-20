from app.opertaions import Sum, Subtract, Multiply, Divide


def test_sum():
    s = Sum()
    assert s.execute(5, 123) == 128


def test_subtract():
    s = Subtract()
    assert s.execute(5, 123) == -118


def test_multiply():
    m = Multiply()
    assert m.execute(5, 123) == 615


def test_divide():
    d = Divide()
    assert d.execute(50, 10) == 5
