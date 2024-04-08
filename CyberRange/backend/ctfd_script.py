from time import sleep

import requests

creds = {"username": 'testing', "password": '<PASSWORD>'}
verbose_logging = True
apikey = "<API_KEY>"


def make_a_list():
    state, challenge_results, board = {}, {}, []
    headers = {'Authorization': f'Token {apikey}', 'Content-Type': 'application/json'}
    url = 'http://localhost/api/v1'
    try:
        challengelist = requests.get(url + '/challenges', json='', headers=headers).json()
        scoreboard = requests.get(url + '/scoreboard', json='', headers=headers).json()
    except requests.exceptions.ConnectionError as e:
        print("Error getting CTFd data:", e)
        return

    try:
        for challenge in challengelist['data']:
            challengename = challenge['name']
            winnerlist = []
            challengedetails = \
                requests.get(url + '/challenges/' + str(challenge['id']) + '/solves', headers=headers).json()['data']
            for entry in challengedetails:
                if entry:
                    winnerlist.append((entry['date'], entry['name']))
            winnerlist = sorted(winnerlist, key=lambda x: x[0])
            winnerlist = [x[1] for x in winnerlist]
            # now update the global results dict with the list of teams who completed that challenge
            challenge_results[challengename] = winnerlist
        state['challenges'] = challenge_results
        for university in scoreboard['data']:
            position = university['pos']
            universityname = university['name']
            universityscore = university['score']
            board.append((position, universityname, universityscore))
        state['leaderboard'] = board
    except KeyError:
        try:
            print('Error: ' + challengelist['errors'])
        except KeyError:
            print('Error: ' + str(challengelist))
    except requests.exceptions.ConnectionError as e:
        print("Error getting CTFd data:", e)
        return
    return state


def main():
    while True:
        state = make_a_list()
        if verbose_logging: print("Results are: " + str(state))
        sleep(5)
        try:
            res = requests.post('https://leaderboarded.club/update', json=state,
                                auth=(creds['username'], creds['password']))
            if res.ok:
                if verbose_logging: print('response from server:', res.text)
        except requests.exceptions.ConnectionError as e:
            print("Error updating leaderboard:", e)
            continue


if __name__ == '__main__':
    main()
