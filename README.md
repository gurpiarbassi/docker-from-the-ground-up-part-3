# docker-from-the-ground-up-part-3
Content for the Docker Birmingham Meetup 14/11/2018

## Overview
This contains resources for a Vagrant / Virtualbox Docker Swarm Lab, and a set of supporting Stackfiles 
to deploy an EFK stack and simple RabbitMQ cluster with some simple clients.

## Slides

Can be found in Pdf for in this repo and in google slides [here](https://docs.google.com/presentation/d/1VJ5cCW5VufOW4Mrc86y59KIs3letHvrNeFSg2mLRlFk/edit?usp=sharing)

There is a section at the end with some links to online tutorials which cover many aspects of the Docker technology ecosystem in an interactive way, many without having to install Docker locally.
Here's the list for easy access ;)

* https://www.katacoda.com/courses/docker-orchestration
* https://container.training/swarm-selfpaced.yml.html
* https://training.play-with-docker.com/
* https://docs.docker.com/engine/swarm/

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
