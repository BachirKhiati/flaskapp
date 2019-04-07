#!/usr/bin/env bash
echo "######################################"
echo "######################################"
echo "Update ubuntu"
apt-get -y update
sudo locale-gen en_US.UTF-8
sudo update-locale LANG=en_US.UTF-8
sudo hostnamectl set-hostname firenoid
echo "######################################"
echo "######################################"
echo "Update repo for PostgreSQL"
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -sc)-pgdg main" > /etc/apt/sources.list.d/PostgreSQL.list'
echo "#######"
echo "#######"
echo "#######"


echo "######################################"
echo "######################################"
echo "Install updates"
sudo apt-get update
echo "#######"
echo "#######"
echo "#######"


echo "######################################"
echo "######################################"
echo "Server: creating user"
sudo adduser app --gecos "First Last,RoomNumber,WorkPhone,HomePhone" --disabled-password
sudo echo 'app  ALL=(ALL:ALL) ALL' >> /etc/sudoers
sudo usermod -aG sudo app
echo "app:Qaz123Wsx456Edc789#@" | sudo chpasswd
cd /home/app
sudo chown -R app:app /home/app/
sudo mkdir -p /home/app/.ssh
sudo touch /home/app/.ssh/authorized_keys
sudo chown app:app /home/app/.ssh
sudo chown app:app /home/app/.ssh/authorized_keys
sudo chmod 700 /home/app/.ssh
sudo chmod 600 /home/app/.ssh/authorized_keys
sudo echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDPUyI68Fho09KapEWWWPymUho1o7Ril1v6rDkyKx3VXMhVH9cX8Ke8gjYvpaeo0/hZTJup6nXu9AVmsZ3Vs4mnzPwRTWvSodT5TbCi0a+NRYdt4S0mlc3xgpQHDoe2IBdQfhDZCqlZ2+0Cfr+2U9+NlTXNolZNmOdOd1MX1xZOWAukS2YegfxnrwrP1K6op0/jZfsWaXVT05r0rlvwC8aXnxE355gzY2VXoM0/9OkBx5RrmZeqQpCAXOXTKIYCYr0NE+ukpo3JEnhA/JwIb6LTxAwC2CYC6bqyejiGkGTQ11OZ1yWingkW61GUkxbJpDGKR7rnZQucKBrAL8WahvaF/X3yITF8pBV4aVx9/99AytvYIlwBDbuWyTOcI9YM+aLM/PsfsIACvZlC0c5TYzEnUtSi1LuOOMnxnakqF11+Ll/TXhl97RwPQSieTjHgmyD/0Wf+HjX05nhM/3rxXVLcV8zKF4wEVzTEoPcv+hhUt6W2yhj1Vq4JH0gR/6Sx5H/2pJ5pg96lb20bz055Rd4ctxt8GlASH1DzjIqzGRxnUfUkbuY5l6IH/2PMAiiXmvBSLRqTdIt1TCoze1kxzVaS8EFUlcIAV6tbI8yEq4XDL/6tZjhFiijp2/vPjrwJzOnhUggbsTF80912DdWfPizbmalIrvl8/GDnYEGcfDFfbw== bachir.khiati@gmail.com" >> /home/app/.ssh/authorized_keys
sudo service ssh restart
echo "#######"
echo "#######"
echo "#######"


echo "######################################"
echo "######################################"
echo "Install the PostgreSQL"
sudo apt-get install -y postgresql-11 postgresql-contrib-11
sudo sed -i "s/#Port 22/Port 2222/" /etc/postgresql/11/main/postgresql.conf
sudo sed -i "s/#ListenAddress 0.0.0.0/#ListenAddress 130.234.130.63/" /etc/postgresql/11/main/postgresql.conf
echo "#######"
echo "#######"
echo "#######"


echo "######################################"
echo "######################################"
echo "PostgreSQL: creating user vagrant/vagrant"
sudo -u postgres psql -c "CREATE USER app WITH SUPERUSER CREATEDB LOGIN ENCRYPTED PASSWORD 'Qaz123Wsx456Edc789#@'"
echo "#######"
echo "#######"
echo "#######"


echo "######################################"
echo "######################################"
echo "PostgreSQL: creating vagrant database"
sudo su postgres -c "createdb -E UTF8 -T template0 --locale=en_US.utf8 -O app app"
echo "#######"
echo "#######"
echo "#######"

echo "######################################"
echo "######################################"
echo "PostgreSQL: installing uuid-ossp extension in app"
sudo -u postgres psql -d app -c 'CREATE EXTENSION "uuid-ossp"'
echo "#######"
echo "#######"
echo "#######"


echo "######################################"
echo "######################################"
echo "PostgreSQL: restarting "
sudo /etc/init.d/postgresql restart
echo "#######"
echo "#######"
echo "#######"


echo "######################################"
echo "######################################"
echo "PostgreSQL: DONE"
echo "PostgreSQL: to connect to the database server from your host,"
#sudo -su root
sudo sed -i "s/#listen_addresses = 'localhost'/listen_addresses = '*' #/" /etc/postgresql/11/main/postgresql.conf
sudo cp /root/dev/db/pg_hba.conf /etc/postgresql/11/main/pg_hba.conf
sudo ss -tunelp | grep 5432
echo "#######"
echo "#######"
echo "#######"


# Restar de DB
sudo /etc/init.d/postgresql restart

###############################################################
###############################################################
###############################################################
###############################################################


sudo apt install -y python3-venv nginx python3-pip python3-dev libpcre3 libpcre3-dev
cd /home/app
sudo python3 -m venv venv
source venv/bin/activate
sudo pip3 install -r /home/vagrant/www/app/requirements.txt
deactivate
rm /etc/nginx/sites-enabled/default
sudo cp /root/dev/app/nginx/app /etc/nginx/sites-available/app
ln -s /etc/nginx/sites-available/app /etc/nginx/sites-enabled
sudo cp /home/app/app.service  /etc/systemd/system/app.service
sudo systemctl start app
sudo systemctl enable app
sudo ufw delete allow 5000
#sudo ufw allow 'Nginx Full'
#sudo systemctl restart nginx
#echo "done release"
#cd /home/app
#source venv/bin/activate
#python /home/app/app.py


