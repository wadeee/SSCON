from flask import Flask, request
from jinja2 import Environment, select_autoescape, FileSystemLoader
import os
import json

app = Flask(__name__)
loader = FileSystemLoader('templates')
env = Environment(loader=loader, autoescape=select_autoescape(['html']))


@app.route('/')
def index():
    template = env.get_template('index.html')
    result = template.render()
    return result


@app.route('/add', methods=['post'])
def add():
    port = request.json.get('port')
    password = request.json.get('password')
    ssconfigfilepath = '/etc/shadowsocks-' + port + '.json'
    ssserviceconfigfilepath = '/etc/systemd/system/shadowsocks-' + port + '.service'

    ssconfig = {'server': "0.0.0.0",
                'server_port': port,
                'password': password,
                'timeout': 600,
                'method': "aes-256-cfb"}

    ssserviceconfig = [
        '[Unit]\n',
        'Description=Shadowsocks-' + port + '\n',
        '[Service]\n',
        'TimeoutStartSec=0\n',
        'ExecStart=/usr/bin/ssserver -c ' + ssconfigfilepath + '\n',
        '[Install]\n',
        'WantedBy=multi-user.target\n'
    ]

    with open('C:/temp' + ssconfigfilepath, 'w') as ssconfigfile, open('C:/temp' + ssserviceconfigfilepath, 'w') as ssserviceconfigfile:
        ssconfigfile.writelines(json.dumps(ssconfig))
        ssserviceconfigfile.writelines(ssserviceconfig)

    os.system('systemctl enable shadowsocks-' + port)
    os.system('systemctl start shadowsocks-' + port)

    return ""


if __name__ == '__main__':
    app.run()
