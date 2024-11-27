from numb3rs import validate


def valid_tests():
    assert validate("100.255.255.255") == True
    assert validate("222.211.200.199") == True
    assert validate("231.0.0.1") == True

def invalid_tests():
    assert validate("1277.0.0.1") == False
    assert validate("222.211.200.1999") == False
    assert validate("231.00000.0000.1") == False

def invalid_format_tests():
    assert validate("cat") == False
    assert validate("dog") == False
    assert validate("cow") == False
