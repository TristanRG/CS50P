from plates import is_valid

def test_positive():
    assert is_valid("CS50") == True

def test_numeric():
    assert is_valid("50324") == False
    assert is_valid("CS50P") == False
    assert is_valid("CS05") == False


def test_case_insensitivity():
    assert is_valid("0GKra") == False

def test_punctuation():
    assert is_valid("CS50.") == False

def test_length():
    assert is_valid("K") == False


