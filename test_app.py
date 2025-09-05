from app import soma

def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0
    assert soma(0, 0) == 0

def test_multiplica():
    assert soma(2, 3) == 6
    assert soma(1, 1) == 1
    assert soma(10, 0) == 0