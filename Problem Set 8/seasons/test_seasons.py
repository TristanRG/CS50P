from datetime import date
from seasons import date_of_birth, convert_text
import pytest

def test_positive():
    assert date_of_birth("2002-04-01") == round((date.today() - date(2002, 4 , 1)).total_seconds() / 60)

    with pytest.raises(SystemExit):
        date_of_birth("")

def test_convert_text():
    assert convert_text(2000) == "Two thousand minutes"
    assert convert_text(1) == "One minutes"
