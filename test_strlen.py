import pytest
from strlen import strlen

@pytest.mark.parametrize("a, expected", [
    ("", 0),
    ("     ", 5),
    ("1234567890", 10),
    ("1234567890" 
     "1234567890", 20),
])

def test_strlen(a, expected):
    assert strlen(a) == expected
