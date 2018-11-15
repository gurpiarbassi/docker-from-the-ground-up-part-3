# -*- mode: ruby -*-
# vi: set ft=ruby :
#

# Set below the number of workers in your Swarm custer
NUM_OF_WORKERS=3

@initManager = <<EOD
if [ ! -d "swarm-token" ]; then
  chown vagrant /var/www/html
  mkdir /var/www/html/swarm-token

  cp /vagrant/registry/daemon.json /etc/docker/daemon.json
  service docker restart  --token `curl -sS 192.168.50.100/swarm-token/worker`
    
  # Init the manager
  docker swarm init --advertise-addr 192.168.50.100:2377

  # Get the worker join token and write a file which is served over http
  # This will make the worker swarm token available to all!
  # Don't do this in production!  Use a secrets manager such as Hashicrop Vault
  docker swarm join-token -q worker > /var/www/html/swarm-token/worker 

  # Deploy management tools stack
  docker stack deploy -c /vagrant/registry/docker-compose.yml registry-mirror

  # Deploy management tools stack
  docker stack deploy -c /vagrant/portainer/docker-compose.yml portainer
fi
EOD

@initWorker = <<EOD
  cp /vagrant/registry/daemon.json /etc/docker/daemon.json
  service docker restart  --token `curl -sS 192.168.50.100/swarm-token/worker` 
  docker swarm join \
    --token `curl -sS 192.168.50.100/swarm-token/worker` \
    192.168.50.100:2377
EOD

Vagrant.configure(2) do |config|
  config.vm.box = "mattjtodd/docker-bionic64"

  config.vm.provider "virtualbox" do |v|
    v.memory = 2048
    v.cpus = 1
  end

  config.vm.define "swarm-manager", primary: true do |manager|
    manager.vm.hostname = "swarm-manager"
    manager.vm.network "private_network", ip: "192.168.50.100"
    manager.vm.provision "docker"
    manager.vm.provision "shell", inline: @initManager
    manager.vm.provider("virtualbox") { |vb| vb.name = "dftgu-3-#{manager.vm.hostname}-#{Time.now.to_i}" }
  end

  (1..NUM_OF_WORKERS).each do |workerNumber|
    config.vm.define "swarm-worker-#{workerNumber}" do |worker|
      worker.vm.hostname = "swarm-worker-#{workerNumber}"
      worker.vm.network "private_network", ip: "192.168.50.#{100+workerNumber}"
      worker.vm.provision "docker"
      worker.vm.provision "shell", inline: @initWorker
      worker.vm.provider("virtualbox") { |vb| vb.name = "dftgu-3-#{worker.vm.hostname}-#{Time.now.to_i}" }
    end
  end
end