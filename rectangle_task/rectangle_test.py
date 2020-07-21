import pytest

class rectangle_class:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def compute_area(self, width, height):
        return width * height

test_rectangle = rectangle_class(3,4)

def test_area():
    assert test_rectangle.compute_area(test_rectangle.width, test_rectangle.height) == 12