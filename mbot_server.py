import serial
from flask import Flask, request
from flask_cors import CORS

# Replace 'COM3' with your mBot USB port
mbot = serial.Serial('COM7', 115200, timeout=1)

app = Flask(__name__)
CORS(app)  # allows your web page to send requests

# Map commands to mBot bytes (example)
command_bytes = {
    "forward": b'\x01',
    "backward": b'\x02',
    "left": b'\x03',
    "right": b'\x04',
    "stop": b'\x00'
}

@app.route('/move', methods=['POST'])
def move():
    data = request.json
    command = data.get('command')
    if command in command_bytes:
        mbot.write(command_bytes[command])
        return {"status": "ok", "command": command}
    return {"status": "error", "message": "Invalid command"}

if __name__ == '__main__':
    print("Starting mBot server...")
    app.run(host='0.0.0.0', port=5000)
