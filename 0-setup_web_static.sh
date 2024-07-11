#!/usr/bin/env bash
# This script sets up Nginx web servers for deployment on multiple servers.
# Ensure to run this script on each server.

WEBSTATIC=$'\\\tlocation /hbnb_static/ {\n\\\t\talias /data/web_static/current/;\n\\\t}\n'

sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo "This tests index.html on Nginx config" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i "35i $WEBSTATIC" /etc/nginx/sites-available/default
sudo service nginx start
