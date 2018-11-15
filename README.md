# docker-from-the-ground-up-part-3
Content for the Docker Birmingham Meetup 14/11/2018

## Overview
This contains resources for a Vagrant / Virtualbox Docker Swarm Lab, and a set of supporting Stackfiles 
to deploy an EFK stack and simple RabbitMQ cluster with some simple clients.

### Getting Started
* Install Vagrant, Virtualbox and Docker.
* Open a sh terminal in the root of this project.
* Bring up the cluster up and create some SSH port forwards by running the `startup.sh` script.
This will leave an ssh terminal session open on the `swarm-manager` and the port mappings on place until this terminates.
* The docker port is mapped to a local port on by (not very secure!) and can be used by the client via
`export DOCKER_HOST=localhost:9999`.
* `docker ps` will now be operating on the manager in the vagrant vm swarm manager.
* Deploy stacks to the cluster whilst having access to your local machine

### Clean Up
* Exceute the script `cleanup.sh` or excute `vagrant destroy -f`
