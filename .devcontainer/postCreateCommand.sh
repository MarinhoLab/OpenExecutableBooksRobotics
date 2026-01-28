#!/bin/bash
set -e

dpkg-reconfigure debconf --frontend=noninteractive

apt-get update
apt-get install -y sudo
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y git python3 python3-pip curl

# This is expected to be run at the root of the repository
pwd
export PIP_BREAK_SYSTEM_PACKAGES=1
python3 -m pip install jupyter-book --pre

curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
NVM_DIR="/.jbdevcontainer/config/nvm"
export NVM_DIR="$NVM_DIR"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
nvm install 24

chmod +x start_from_devcontainer.sh