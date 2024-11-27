from working import convert
import pytest

def test_positive():
    assert convert("08:00 AM to 05:00 PM") == "08:00 to 17:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("01:00 PM to 11:59 PM") == "13:00 to 23:59"

def test_negative():
    with pytest.raises(ValueError):
        convert("13:00 AM to 02:00 PM")
    with pytest.raises(ValueError):
        convert("11:00 PM to 24:00 AM")
    with pytest.raises(ValueError):
        convert("11:00 to 12:00 PM")
    with pytest.raises(ValueError):
        convert("11:00AMto12:00PM")
