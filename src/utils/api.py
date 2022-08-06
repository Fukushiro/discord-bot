from array import array
import requests
import os


def get_blocked_users():
    try:
        base_url = os.getenv("BASE_URL")
        blocked_users = requests.get(f'{base_url}/block/get/all')
        data = blocked_users.json()['data']
        blocked_users = [d['username'] for d in data if d['isBlocked'] == 1]

        return blocked_users
    except:
        return None


def block_user(username, isBlocked):
    try:
        base_url = os.getenv("BASE_URL")
        dataDic = {
            "username": username,
            "isBlocked": isBlocked
        }
        print(dataDic)
        retorno = requests.put(f'{base_url}/block/block', json=dataDic)
        print(retorno.json())
        if retorno.status_code == 200:
            return True
        else:
            return False
    except:
        return False
