#!/bin/bash

# While 2.0 is not stable
python -m pip install jupyter-book --pre

# Otherwise the links will not be correctly set up for the webpage
export BASE_URL="https://marinholab.github.io/OpenExecutableBooksRobotics"

cat myst.yml
python -m jupyter book build --html --execute
