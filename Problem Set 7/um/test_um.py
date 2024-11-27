from um import count


def test_positive():
    assert count("um um um") == 3
    assert count("um how about going um") == 2
    assert count("um ") == 1
    assert count("UM UM ") == 2


def test_negative():
    assert count("yum") == 0
    assert count("hey there yummy") == 0
    assert count("cat ") == 0
    assert count("CAt ") == 0
