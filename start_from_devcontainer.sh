export NVM_DIR="/.jbdevcontainer/config/nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
python3 -m jupyter book build --html