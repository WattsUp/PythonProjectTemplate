"""Setup and install project_template

Typical usage:
  python setup.py develop
  python setup.py install
  python setup.py test
"""

import setuptools

module_folder = "project_template"
module_name = "PythonProjectTemplate"

with open("README.md", encoding="utf-8") as file:
  longDescription = file.read()

required = []
extras_require = {
    "test": ["AutoDict", "coverage", "pylint", "numpy"],
    "dev": [
        "AutoDict", "coverage", "pylint", "numpy", "toml", "witch-ver", "yapf"
    ]
}

setuptools.setup(
    name="PythonProjectTemplate",
    use_witch_ver=True,
    description="A template repository for Python projects",
    long_description=longDescription,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=setuptools.find_packages(exclude=["tests", "tests.*"]),
    package_data={module_folder: []},
    install_requires=required,
    extras_require=extras_require,
    test_suite="tests",
    scripts=[],
    author="Bradley Davis",
    author_email="me@bradleydavis.tech",
    url="https://github.com/WattsUp/PythonProjectTemplate",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
    # include_package_data=True, # Leave out cause wacky
    zip_safe=False,
    entry_poiints={"console_scripts": []})
