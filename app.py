import json
import os
import subprocess
import time

import requests
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def receive_message():
    data = request.json
    proc = subprocess.Popen(
        ['bash', 'install_python_package.sh', data['package']],
        stdout=subprocess.PIPE)
    out, err = proc.communicate()
    print(out)
    return out, 204


if __name__ == '__main__':
    port = 5000
    app.run(port=port)
