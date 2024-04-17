import random
from time import sleep
import requests
from werkzeug.security import generate_password_hash

creds = {"username": 'testing', "password": 'obi0r6Ljy4hdmZzZyX58EZS9jd0qRM8PyXLbAIpkoD8K1gaqqQNTvDbs1oncetNn'}

challenges = ["Another Name", "Fusion", "Snake Escape", "Cyber Cooking", "Mysterious", "Let me in!"]
teams = ["BSU", "CEI", "CSI", "CWI", "ISU", "ICSC", "NIC", "UI"]


while True:
    sleep(5)
    try:
        data = {"leaderboard": [], "challenges": {}}
        for challenge in challenges:
            winning_teams = random.sample(teams, random.randint(0, 6))
            data["challenges"][challenge] = winning_teams
        for team in teams:
            data["leaderboard"].append((random.randint(1, 10), team, random.randint(0, 10000)))
        res = requests.post('http://localhost:5000/update', json=data,
                            auth=(creds['username'], creds['password']))
        print('Data sent to server:', data)
        print('response from server:', res.text)
        # dictFromServer = res.json()
    except requests.exceptions.ConnectionError as e:
        print("Error updating leaderboard:", e)
        continue
