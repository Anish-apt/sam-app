import cal


def test_add():
    total =  cal.add(4,5)
    assert total == 9


def test_subtract():
    total = cal.subtract(6,5)
    assert total == 1


def test_multiply():
    total = cal.multiply(4,5)
    assert total == 20


def test_divide():
    total = cal.divide(6,2)
    assert total == 3
