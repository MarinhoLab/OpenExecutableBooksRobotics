#!/bin/bash

# While 2.0 is not stable
python -m pip install jupyter-book --pre

# Otherwise the links will not be correctly set up for th webpage
export BASE_URL="https://marinholab.github.io/OpenExecutableBooksRobotics/"

# This is a bit hacky.
# https://github.com/orgs/jupyter-book/discussions/2055#discussioncomment-13250715
# This is my temporary hacky solution

# Run once without the devel
cp myst.yml _myst.yml
sed -i.bak '/#USING DQROBOTICS DEVEL [START]/,/#USING DQROBOTICS DEVEL [END]/d' myst.yml
cat myst.yml
python -m jupyter book build --html --execute

# Run again with the devel. The cached should no longer collide
cp mv _myst.yml myst.yml
python -m jupyter book build --html --execute

