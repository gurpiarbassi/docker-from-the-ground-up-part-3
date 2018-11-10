#!/usr/bin/env bash

set -ex

vagrant up

exec ./ssh-port-forward.sh
