import requests
import os

url = 'http://127.0.0.1:8000/'
username = 'ra'
password = 'rarara'

def get_token():
    login_url = url + 'api/v2/login'
    data = dict()
    data = {'name':username, 'password':password}
    r = requests.post(login_url, json=data)
    r_json = r.json()
    token = r_json['token']
    return token

def get_datasets():
    token = get_token()
    headers = {'Authorization': 'Bearer ' + token }
    datasets_url = url + 'api/v2/datasets'
    datasets = requests.get(datasets_url, headers=headers)
    print('done')


if __name__ == "__main__":
    ds = get_datasets()
    t = get_token()
    print('done')