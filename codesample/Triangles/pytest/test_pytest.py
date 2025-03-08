import pytest
from triangle_sides import triangle

def test_equilateral_triangle():
    assert triangle(2, 2, 2) == 'equilateral'
    assert triangle(10, 10, 10) == 'equilateral'

def test_isosceles_triangle():
    assert triangle(3, 4, 4) == 'isosceles'
    assert triangle(4, 3, 4) == 'isosceles'
    assert triangle(4, 5, 3) == 'isosceles'
    assert triangle(10, 10, 2) == 'isosceles'

def test_scalene_triangle():
    assert triangle(3, 4, 5) == 'scalene'
    assert triangle(10, 11, 12) == 'scalene'
    assert triangle(5, 4, 2) == 'scalene'