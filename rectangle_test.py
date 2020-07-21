import pytest
import rectangle
import random

def test_area():
    for i in range(20):
        new_rectangle = rectangle.rectangle(random.random(),random.random())
        assert new_rectangle.compute_area(getattr(new_rectangle,"width"),getattr(new_rectangle,"height")) == getattr(new_rectangle,"width")*getattr(new_rectangle,"height")