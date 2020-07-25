import pytest
import factors

def test_factorials():
    assert factors.factorials(15) == [3, 5]
    assert factors.factorials(12) == [2,3,4,6]