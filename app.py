import subprocess

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
    app.run(debug=True, port=5000)
