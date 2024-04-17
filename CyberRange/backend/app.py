import flask
from flask import Flask, send_from_directory
from flask_httpauth import HTTPBasicAuth
from waitress import serve
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()
state = {}
users = {"testing": generate_password_hash("obi0r6Ljy4hdmZzZyX58EZS9jd0qRM8PyXLbAIpkoD8K1gaqqQNTvDbs1oncetNn"), }

mapping = {'Another Name': 'another_name', 'Fusion': 'cold_fusion', 'Snake Escape': 'snake_escape',
           'Let me in!': 'let_me_in', 'Mysterious': 'mysterious', 'Cyber Cooking': 'cyber_cooking'}

example_state = {
    'challenges': {'Another Name': ['ISU'], 'Fusion': ['ISU', 'CWI'], 'Snake Escape': ['CWI'], 'Let me in!': ['CWI'],
                   'Mysterious': ['CWI'], 'Cyber Cooking': ['CWI']}, 'leaderboard': [(1, 'CWI', 3920), (2, 'ISU', 1010)]}

state = example_state


@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username


@app.route('/')
def index():
    # return send_from_directory('/var/www/leaderboard', 'index.html') # for prod
    return send_from_directory('../CyberRange/dist', 'index.html')

# Remove this for prod, since Nginx will be serving all the static files
@app.route('/<path:path>')
def serve_main_js(path):
    return send_from_directory('..\\CyberRange\\dist', path)


@app.route('/update', methods=['POST'])
@auth.login_required
def write_update():
    global state
    print(f'Updating: {flask.request.data}')
    state = flask.request.get_json()
    return 'Request received', 200


@app.route('/api/challenge_state', methods=['GET'])
def read_challenge_state():
    global state
    return state['challenges'], 200


@app.route('/api/mapping', methods=['GET'])
def read_mapping():
    global mapping
    return mapping, 200


@app.route('/api/leaderboard', methods=['GET'])
def read_leaderboard():
    global state
    print(state)
    return state['leaderboard'], 200


if __name__ == '__main__':
    # app.run(debug=True)
    serve(app, host='127.0.0.1', port=5000)
