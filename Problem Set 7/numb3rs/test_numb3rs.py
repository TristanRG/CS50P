from numb3rs import validate


def test_range():
    assert validate("20.260.15.35") is False
    assert validate("20.199.15.35") is True
    assert validate("20.198.15.35") is True
    assert validate("20.197.15.35") is True
    assert validate("20.196.15.35") is True
    assert validate("20.195.15.35") == True
