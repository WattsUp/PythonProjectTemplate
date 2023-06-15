"""Test base class
"""

import pathlib
import shutil
import string
import time
import unittest

import autodict
import numpy as np

from tests import TEST_LOG


class TestBase(unittest.TestCase):
  """Test base class
  """

  _TEST_ROOT = pathlib.Path(".test")
  _DATA_ROOT = pathlib.Path(__file__).parent.joinpath("data")
  _P_FAIL = 1e-4
  _RNG = np.random.default_rng()

  @classmethod
  def random_string(cls, length: int = 20) -> str:
    """Generate a random string a-zA-Z

    Args:
      length: Length of string to generate

    Returns:
      Random string
    """
    return "".join(list(cls._RNG.choice(list(string.ascii_letters), length)))

  def __clean_test_root(self):
    """Clean root test folder
    """
    if self._TEST_ROOT.exists():
      shutil.rmtree(self._TEST_ROOT)

  def assertEqualWithinError(self, target, real, threshold):
    """Assert if target != real within threshold

    Args:
      target: Target value
      real: Test value
      threshold: Fractional amount real can be off
    """
    if target == 0.0:
      error = np.abs(real - target)
    else:
      error = np.abs(real / target - 1)
    self.assertLessEqual(error, threshold)

  def setUp(self):
    self.__clean_test_root()
    self._TEST_ROOT.mkdir(parents=True, exist_ok=True)
    self._test_start = time.perf_counter()

    # Remove sleeping by default, mainly in read hardware interaction
    self._original_sleep = time.sleep
    time.sleep = lambda *args: None

  def tearDown(self):
    duration = time.perf_counter() - self._test_start
    with autodict.JSONAutoDict(TEST_LOG) as d:
      d["methods"][self.id()] = duration
    self.__clean_test_root()

    # Restore sleeping
    time.sleep = self._original_sleep

  def log_speed(self, slow_duration: float, fast_duration: float):
    """Log the duration of a slow/fast A/B comparison test

    Args:
      slow_duration: Duration of slow test
      fast_duration: Duration of fast test
    """
    with autodict.JSONAutoDict(TEST_LOG) as d:
      d["speed"][self.id()] = {
          "slow": slow_duration,
          "fast": fast_duration,
          "increase": slow_duration / fast_duration
      }

  @classmethod
  def setUpClass(cls):
    print(f"{cls.__module__}.{cls.__qualname__}[", end="", flush=True)
    cls._CLASS_START = time.perf_counter()

  @classmethod
  def tearDownClass(cls):
    print("]done", flush=True)
    # time.sleep(10)
    duration = time.perf_counter() - cls._CLASS_START
    with autodict.JSONAutoDict(TEST_LOG) as d:
      d["classes"][f"{cls.__module__}.{cls.__qualname__}"] = duration
