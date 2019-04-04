#!/usr/bin/env bash
apt-get -y update
sudo apt-get install -y python3-pip python3-dev libpcre3 libpcre3-dev
sudo pip3 install virtualenv
apt-get  install -y nginx
cd /vagrant
virtualenv venv
source venv/bin/activate
pip3 install -r /vagrant/requirements.txt
deactivate
cd /home/vagrant
mkdir www
ln -s /vagrant /home/vagrant/www/app
rm /etc/nginx/sites-enabled/default
sudo cp /home/vagrant/www/app/templates/nginx/app /etc/nginx/sites-available/app
ln -s /etc/nginx/sites-available/app /etc/nginx/sites-enabled
#sudo cp /home/vagrant/www/app/app.service  /etc/systemd/system/app.service
#sudo systemctl start app
#sudo systemctl enable app
#sudo ufw delete allow 5000
sudo ufw allow 'Nginx Full'
sudo systemctl restart nginx
echo "done release"
cd /home/vagrant/www/app
source venv/bin/activate
export FLASK_ENV=development
python3 /home/vagrant/www/app/app.py