#python -m waitress --host=127.0.0.1 --port=5000 app:app


import flask
from flask import Flask, send_from_directory, jsonify, request
from waitress import serve
import os

app = Flask(__name__)
leaderboard_state = []

school_logo_mapping = {
    "BSU": "bsu.jpg",
    "CEI": "cei.png",
    "CSI": "csi.png",
    "CWI": "cwi.png",
    "ISU": "isu.png",
    "ICSC": "Icsc.png",
    "NIC": "nic.png",
    "UI": "ui.jpg"
}

@app.route('/')
def index():
    return send_from_directory('..\\CyberRange\\dist', 'index.html')

@app.route('/<path:path>')
def serve_main_js(path):
    return send_from_directory('..\\CyberRange\\dist', path)

@app.route('/update', methods=['POST', 'GET'])
def update():
    global leaderboard_state
    if request.method == 'POST':
        data = request.json
        if data:
            leaderboard_state = data
            print("Data received:", leaderboard_state)
            return jsonify({"message": "Leaderboard updated successfully."}), 200
        else:
            return jsonify({"error": "No data received."}), 400
    elif request.method == 'GET':
        return jsonify(leaderboard_state), 200


if __name__ == '__main__':
    # app.run(debug=True)
    serve(app, host='0.0.0.0', port=5000)
