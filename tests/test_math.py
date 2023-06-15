"""Test module project_template.math
"""

from project_template import math

from tests import base


class TestMathMethods(base.TestBase):
  """Test math methods
  """

  def test_add_int(self):
    self.assertEqual(math.add_int(1, 4), 5)
    self.assertNotEqual(math.add_int(-1, 4), 5)
