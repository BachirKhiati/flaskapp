# -*- mode: ruby -*-
# vi: set ft=ruby :
APP_BOXNAME = "flask-app"
APP_IP = "192.168.1.18"

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  config.vm.box = "bittercold/ubuntu-17.10"
  config.vm.define APP_BOXNAME
  config.vm.network "public_network", use_dhcp_assigned_default_route: true
  config.vm.provider "virtualbox" do |vb|
     vb.gui = false
     vb.memory = "1024"
     vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
     vb.customize ["modifyvm", :id, "--natdnsproxy1", "on"]


  config.vm.provision "script_a", type: "shell" do |s|
          s.path = "templates/scripts.sh"
          s.upload_path = "/tmp/scripts.sh"
           end
  end

end