from bank import value

def test_hello():
    assert value("hello") == 0

def test_case_insensitivity():
    assert value("HeLLo") == 0

def test_hey():
    assert value("hey") == 20

def test_otherwise():
    assert value("otherwise") == 100

def test_number():
    assert value("123") == 100

def test_punctuation():
    assert value("...") == 100

