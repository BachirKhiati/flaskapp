# -*- mode: ruby -*-
# vi: set ft=ruby :
APP_BOXNAME = "flask-app"
DB_BOXNAME = "db-app"
APP_IP = "192.168.1.18"
DB_IP = "192.168.1.19"

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  config.vm.define DB_BOXNAME do |db|
        db.vm.box = "generic/ubuntu1804"
        db.vm.define DB_BOXNAME
        db.vm.box_check_update = false
  	    db.vm.network "public_network", ip: DB_IP
  	    db.vm.network :forwarded_port, guest: 5432, host: 5433

  	    db.vm.synced_folder "appflask/templates/dev/db", "/home/vagrant/templates/db"
  	    db.vm.provider 'virtualbox' do |vb|
  	        vb.gui = false
            vb.memory = "1024"
            vb.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
            vb.customize ['modifyvm', :id, '--cableconnected1', 'on']
            vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
            vb.customize ["modifyvm", :id, "--natsettings1", "16000,64,64,1024,1024"]
            vb.customize ["modifyvm", :id, "--nictype1", "virtio"]
            vb.customize ["modifyvm", :id, "--nataliasmode1", "sameports"]
        end

        db.vm.provision "script_a", type: "shell" do |s|
                  s.path = "appflask/templates/db_vagrant_setup.sh"
                  s.upload_path = "/tmp/db_vagrant_setup.sh"
        end
  end

  config.vm.define APP_BOXNAME  do |app|
        app.vm.box = "generic/ubuntu1804"
        app.vm.define APP_BOXNAME
        app.vm.network "public_network", ip: APP_IP
        app.vm.synced_folder "./", "/home/vagrant/www/app"
        app.vm.provider "virtualbox" do |vb|
            vb.gui = false
            vb.memory = "1024"
            vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
            vb.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
        end

        app.vm.provision "script_a", type: "shell" do |s|
                  s.path = "appflask/templates/app_vagrant_setup.sh"
                  s.upload_path = "/tmp/scripts.sh"
          end
  end

end