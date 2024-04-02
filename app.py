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
    # return a status code
    return out, 204


if __name__ == '__main__':
    port = 5000
    ngrok_process = subprocess.Popen(['ngrok', 'http', str(port)],
                                     stdout=subprocess.PIPE)
    time.sleep(1)
    # Get the ngrok tunnel information (ngrok API default port is 4040)
    ngrok_url = "http://localhost:4040/api/tunnels"
    response = requests.get(ngrok_url)
    tunnels = json.loads(response.text)
    # Find the public URL for http forwarding
    public_url = tunnels['tunnels'][0]['public_url']
    print(public_url)
    app.run(port=port, debug=True, threaded=True)
