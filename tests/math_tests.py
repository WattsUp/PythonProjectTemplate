from project_template import math


def test() -> None:
  """Test project_template.math
  """
  if math.addInt(1, 3) != 4:
    raise Exception("math.addInt failed")