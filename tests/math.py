import unittest

from project_template import math

class TestMathMethods(unittest.TestCase):

  def test_addInt(self):
    self.assertEqual(math.addInt(1, 4), 5)
    self.assertNotEqual(math.addInt(-1, 4), 5)