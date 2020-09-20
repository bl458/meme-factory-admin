import json
import urllib.request
import requests
from os import path


# Log in to new admin session
def login_admin(email, pw):
    url = 'http://localhost:3000/admin/session'
    body = {"email": email, "pw": pw}

    try:
        response = requests.post(url, data=body)
        print('Logged in as admin: ', response.status_code)

        return response.text
    except Exception as err:
        print('Admin Login Error: ', err)


# Upload image files
def upload_files_admin(files, session_token):
    url = 'http://localhost:3000/admin/images'
    headers = {'api-token': session_token}
    files_body = []

    # Initialize body of request
    for file in files:
        file_ext = path.splitext(file)[1][1:]
        files_body.append(('files', (file, open(
            file, 'rb'), 'image/' + file_ext)))

    try:
        response = requests.post(url, files=files_body, headers=headers)
        if response.status_code == 201:
            print()
            for i in range(len(files)):
                print(files[i], response.json()[i]['url'])
                print()
        else:
            print(files, response.json())
    except Exception as err:
        print('Admin Image Upload Error: ', err)
