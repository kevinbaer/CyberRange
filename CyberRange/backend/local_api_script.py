import random
from time import sleep
import requests

# TODO: Update this script
challenges = ["Another Name", "Fusion", "Shell Shocked", "Snake Escape", "???"]
teams = ["BSU", "CEI", "CSI", "CWI", "ISU", "ICSC", "NIC", "UI"]

while True:
    sleep(5)
    try:
        data = {}
        for challenge in challenges:
            winning_teams = random.sample(teams, random.randint(0, 6))
            data[challenge] = winning_teams
        res = requests.post('http://localhost:5000/update', json=data)
        print('Data sent to server:', data)
        print('response from server:', res.text)
        dictFromServer = res.json()
    except requests.exceptions.ConnectionError as e:
        print("Error updating leaderboard:", e)
        continue
