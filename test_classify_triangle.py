import pytest
from classify_triangle import classify_triangle

@pytest.mark.parametrize("a, b, c, expected", [
    (3, 3, 3, "Равносторонний"),
    (4, 4, 4, "Равносторонний"),
    (4, 3, 3, "Равнобедренный"),
    (3, 3, 4, "Равнобедренный"),
    (3, 4, 5, "Разносторонний"),
    (0,0,1, "не треугольник"),
    (1,1,3, "не треугольник"),
    (2,2,4, "не треугольник")])
def test_classify_triangle(a, b, c, expected):
    assert classify_triangle(a, b, c) == expected
