# Python Dependencies

sudo apt update
sudo apt-get install -y git python3-pip python3-dev libpq-dev make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev curl
sudo  update-alternatives --install /usr/bin/python python /usr/bin/python3 1
sudo update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1

sudo pip install virtualenvwrapper

export WORKON_HOME=~/Envs
mkdir -p $WORKON_HOME
source /usr/local/bin/virtualenvwrapper.sh

# Nodejs Dependencies
sudo apt install -y nodejs
sudo apt install -y npm

exec $SHELL
