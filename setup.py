#!/usr/bin/env python

import os
import re
import setuptools
import shutil
import sys

if not sys.version_info >= (3, 4):
  exit("Sorry, Python's version must be later than 3.4.")



# constants

LIBRARY_NAME = "hypar"
README_BASENAME = "README"
RST_EXT = "rst"
MD_EXT = "md"



# functions

def warn(*text):
  print("WARNING:", *text, file=sys.stderr)


def version():
  with open("hypar.py") as f:
    lines = f.readlines()
  return next(re.match(r"__version__\s*=\s*\"((\d|\.)*)\"", line)
              for line in lines if line.startswith("__version__")).group(1)


def read_text_file(filename):
  with open(os.path.join(os.path.dirname(__file__), filename)) as f:
    return f.read()


def readme_text():
  readme_rst = README_BASENAME + "." + RST_EXT
  readme_md = README_BASENAME + "." + MD_EXT

  try:
    import pypandoc
    with open(readme_rst, "w") as f:
      f.write(pypandoc.convert(readme_md, RST_EXT))
    return read_text_file(readme_rst)
  except ImportError as e:
    if os.path.isfile(readme_rst):
      os.remove(readme_rst)
    warn(e)
    shutil.copyfile(readme_md, README_BASENAME)
    return read_text_file(README_BASENAME)



# main routine

def main():
  setuptools.setup(
      name="hypar",
      version=version(),
      description="a library to manage hyper parameters of "
                  "machine learning models",
      long_description=readme_text(),
      license="Public Domain",
      author="raviqqe",
      author_email="raviqqe@gmail.com",
      url="http://github.com/raviqqe/hypar/",
      py_modules=["hypar"],
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Intended Audience :: Science/Research",
          "License :: Public Domain",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Topic :: Scientific/Engineering :: Artificial Intelligence",
      ],
  )


if __name__ == "__main__":
  main()
