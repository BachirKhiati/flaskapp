#!/usr/bin/env bash
apt-get -y update
sudo locale-gen en_US.UTF-8
sudo update-locale LANG=en_US.UTF-8





echo "######################################"
echo "######################################"
echo "######################################"
echo "Update repo for PostgreSQL"
echo "######################################"
echo "######################################"
echo "######################################"
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -sc)-pgdg main" > /etc/apt/sources.list.d/PostgreSQL.list'


echo "######################################"
echo "######################################"
echo "######################################"
echo "Install updates"
echo "######################################"
echo "######################################"
echo "######################################"
sudo apt-get update


echo "######################################"
echo "######################################"
echo "######################################"
echo "Install the PostgreSQL"
echo "######################################"
echo "######################################"
echo "######################################"
sudo apt-get install -y postgresql-11 postgresql-contrib-11
# Create the user to access the db. (vagrant sample)

echo "######################################"
echo "######################################"
echo "######################################"
echo "PostgreSQL: creating user vagrant/vagrant"
echo "######################################"
echo "######################################"
echo "######################################"
sudo -u postgres psql -c "CREATE USER vagrant WITH SUPERUSER CREATEDB LOGIN ENCRYPTED PASSWORD 'vagrant'"

echo "######################################"
echo "######################################"
echo "######################################"
echo "PostgreSQL: creating vagrant database"
echo "######################################"
echo "######################################"
echo "######################################"
sudo su postgres -c "createdb -E UTF8 -T template0 --locale=en_US.utf8 -O vagrant flaskapp"


echo "######################################"
echo "######################################"
echo "######################################"
echo "PostgreSQL: installing uuid-ossp extension in vagrant"
echo "######################################"
echo "######################################"
echo "######################################"
sudo -u postgres psql -d flaskapp -c 'CREATE EXTENSION "uuid-ossp"'

echo "######################################"
echo "######################################"
echo "######################################"
echo "PostgreSQL: restarting "
echo "######################################"
echo "######################################"
echo "######################################"
sudo /etc/init.d/postgresql restart

echo "######################################"
echo "######################################"
echo "######################################"
echo "PostgreSQL: DONE"
echo "PostgreSQL: to connect to the database server from your host,"
echo "######################################"
echo "######################################"
echo "######################################"

sudo sed -i "s/port = 5433/port = 5432/" /etc/postgresql/11/main/postgresql.conf
sudo sed -i "s/#listen_addresses = 'localhost'/listen_addresses = '*' #/" /etc/postgresql/11/main/postgresql.conf
sudo cp /home/vagrant/templates/dev/db/pg_hba.conf /etc/postgresql/11/main/pg_hba.conf

sudo ss -tunelp | grep 5432
# Restar de DB
sudo /etc/init.d/postgresql restart
