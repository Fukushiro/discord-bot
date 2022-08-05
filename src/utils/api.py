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
