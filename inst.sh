#!/bin/sh

#pip install
pip install flask
pip install jinja2
pip install gunicorn

#add sscon to service
echo y | cp ./sscon.service /etc/systemd/system/
systemctl systemctl daemon-reload
systemctl enable sscon
ssytemctl start sscon
