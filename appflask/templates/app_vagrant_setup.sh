#!/usr/bin/env bash
apt-get -y update
sudo apt install -y python3-venv nginx python3-pip python3-dev libpcre3 libpcre3-dev
cd /home/vagrant/www/app
sudo python3 -m venv venv
source venv/bin/activate
sudo pip3 install -r /home/vagrant/www/app/requirements.txt
deactivate
rm /etc/nginx/sites-enabled/default
sudo cp /home/vagrant/www/app/templates/dev/app/nginx/app /etc/nginx/sites-available/app
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
python /home/vagrant/www/app/app.py
