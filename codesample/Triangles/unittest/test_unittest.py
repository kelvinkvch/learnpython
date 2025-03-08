import unittest
from triangle_sides import triangle

class Test_Sides(unittest.TestCase):
    # equilateral triangles have three equal sides
    def test_equilateral_triangle(self):
        self.assertEqual('equilateral', triangle(2, 2, 2))
        self.assertEqual('equilateral', triangle(10, 10, 10))

    # isosceles triangles have two equal sides
    def test_isosceles_triangle(self):
        self.assertEqual('isosceles', triangle(3, 4, 4))
        self.assertEqual('isosceles', triangle(4, 3, 4))
        self.assertEqual('isosceles', triangle(4, 5, 3))
        self.assertEqual('isosceles', triangle(10, 10, 2))

    # scalene triangles have no equal sides
    def test_scalene_triangle(self):
        self.assertEqual('scalene', triangle(3, 4, 5))
        self.assertEqual('scalene', triangle(10, 11, 12))
        self.assertEqual('scalene', triangle(5, 4, 2))