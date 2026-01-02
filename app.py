from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import socket
import time
import threading


PORT = 50286
PORT_ALT = 50787
UP_TIME = 60

app = Flask(__name__)
CORS(app)

def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

# def shutdown_server():
#     time.sleep(UP_TIME)
#     func = request.environ.get('werkzeug.server.shutdown')
#     if func is None:
#         raise RuntimeError('Not running with the Werkzeug Server')
#     func()

@app.route('/send-email', methods=['POST'])
def send_email():
    # data = request.json
    message = request.form.get('message')
    result = subprocess.run(['python3', '/u/yichen/public_html/send_email.py', message], capture_output=True, text=True)
    # return jsonify({'output': result.stdout})
    return result.stdout

if __name__ == '__main__':
    port = PORT
    if is_port_in_use(port):
        print(f"Port {port} is in use, trying another port.")
        port = PORT_ALT  # or any other available port
    # threading.Thread(target=shutdown_server).start()
    app.run(port=port)
