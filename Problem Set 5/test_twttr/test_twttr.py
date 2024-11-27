from twttr import shorten


def main():
    test_positive()

def test_positive():
    assert shorten("twitter") == "twttr"
    assert shorten("mAyBeee") == "myB"
    assert shorten("just_a_test") == "jst__tst"
    assert shorten("1234") == "1234"
    assert shorten("...") == "..."


if __name__ == "__main__":
    main()



