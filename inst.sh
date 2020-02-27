#!/bin/sh

## pip install ##
python3 -m pip install flask
python3 -m pip install jinja2
python3 -m pip install gunicorn

## add sscon to service ##
echo y | cp ./sscon.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable sscon
systemctl start sscon

## add config to nginx ##
echo y | cp ./sscon.nginx.http.conf /etc/nginx/conf.d/
systemctl restart nginx ## please make sure nginx installed ##
