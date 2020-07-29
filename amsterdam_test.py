import pytest
from amsterdam import name

def test_am():
    assert name("Am I in Amsterdam?") == 1
    assert name("I am in Amsterdam am I?") == 2
    assert name("I'm not in Amsterdam") == 0