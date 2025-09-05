from app import soma

def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0
    assert soma(0, 0) == 0

def test_multiplica():
    assert multiplica(2, 3) == 6
    assert multiplica(1, 1) == 1
    assert multiplica(10, 0) == 0