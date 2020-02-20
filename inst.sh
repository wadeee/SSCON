#!/bin/sh

## pip install ##
pip install flask
pip install jinja2
pip install gunicorn

## add sscon to service ##
echo y | cp ./sscon.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable sscon
systemctl start sscon

## add config to nginx ##
echo y | cp ./sscon.nginx.http.conf /etc/nginx/conf.d/
systemctl restart nginx ## please make sure nginx installed ##
