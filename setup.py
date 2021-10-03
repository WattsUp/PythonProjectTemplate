"""Setup and install project_template

Typical usage:
  python setup.py develop
  python setup.py install
  python setup.py test
"""

import numpy
import os
import setuptools

from setuptools import setup, find_packages
import setuptools.command.develop
import setuptools.command.build_py

from tools import gitsemver

module_folder = "project_template"

with open("README.md", encoding="utf-8") as file:
  longDescription = file.read()

with open("requirements.txt", encoding="utf-8") as file:
  required = file.read().splitlines()

version = gitsemver.get_version()
with open(f"{module_folder}/version.py", "w", encoding="utf-8") as file:
  file.write('"""Module version information\n"""\n\n')
  file.write(f'version = "{version}"\n')
  file.write(f'version_full = "{version.full_str()}"\n')

cwd = os.path.dirname(os.path.abspath(__file__))

try:
  from Cython import Build
  cythonize = Build.cythonize
except ImportError:

  def cythonize(*args, **kwargs):
    # Defer import until after setuptools installs it
    from Cython import Build as Build_defer  # pylint: disable=import-outside-toplevel
    return Build_defer.cythonize(*args, **kwargs)


def find_pyx(path="."):
  pyx_files = []
  for root, _, filenames in os.walk(path):
    for f in filenames:
      if f.endswith(".pyx"):
        pyx_files.append(os.path.join(root, f))
  return pyx_files


def find_cython_extensions(path="."):
  extensions = cythonize(find_pyx(path), language_level=3)
  for ext in extensions:
    ext.include_dirs = [numpy.get_include()]
  return extensions


class BuildPy(setuptools.command.build_py.build_py):

  def run(self):
    setuptools.command.build_py.build_py.run(self)


class Develop(setuptools.command.develop.develop):

  def run(self):
    setuptools.command.develop.develop.run(self)


setup(
    name="PythonProjectTemplate",
    version=str(version),
    description="A template repository for Python projects",
    long_description=longDescription,
    long_description_content_type="text/markdown",
    license="MIT",
    ext_modules=find_cython_extensions(),
    packages=find_packages(),
    package_data={module_folder: []},
    install_requires=required,
    tests_require=[],
    test_suite="tests",
    scripts=[],
    author="Bradley Davis",
    author_email="me@bradleydavis.tech",
    url="https://github.com/WattsUp/PythonProjectTemplate",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    include_package_data=True,
    cmdclass={
        "build_py": BuildPy,
        "develop": Develop,
    },
    zip_safe=False,
)
