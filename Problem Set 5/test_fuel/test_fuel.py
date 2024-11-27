from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("1/4") == 25.0
    assert convert("3/4") == 75.0
    assert convert("4/4") == 100.0

def test_errors():
    with pytest.raises(ValueError):
        convert("three/four")
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(25) == "25%"
