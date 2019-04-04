#!/usr/bin/env bash
apt-get -y update
sudo locale-gen en_US.UTF-8
sudo update-locale LANG=en_US.UTF-8
#wget -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
## Create a file with the repository address
#echo deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main | sudo tee /etc/apt/sources.list.d/postgresql.list

wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -sc)-pgdg main" > /etc/apt/sources.list.d/PostgreSQL.list'
# Install the PostgreSQL
sudo apt-get update
sudo apt-get install -y postgresql-11 postgresql-contrib-11
# Create the user to access the db. (vagrant sample)
sudo -u postgres psql -c "CREATE USER vagrant WITH SUPERUSER CREATEDB ENCRYPTED PASSWORD 'vagrant'"
# Change the port
sudo sed -i "s/port = 5433/port = 5432/" /etc/postgresql/11/main/postgresql.conf
sudo ss -tunelp | grep 5432
sudo ss -tunelp | grep 5433
# Restar de DB
sudo /etc/init.d/postgresql restart
