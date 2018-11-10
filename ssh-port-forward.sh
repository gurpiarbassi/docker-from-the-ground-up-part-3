#!/usr/bin/env bash

set -ex

exec vagrant ssh -- -L9999:/var/run/docker.sock \
  -L9000:localhost:9000 \
  -L5601:localhost:5601 \
  -L3000:localhost:3000 \
  -L15672:localhost:15672 \
  -L5000:localhost:5000 \
  -L8080:localhost:8080
