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
        print('\nStarted Admin Image Upload. Check js console for details\n')
        response = requests.post(url, files=files_body, headers=headers)
        if response.status_code == 201:
            print('Admin Image Upload: 201')
            print('Uploaded a total of',
                  len(response.json()), 'images\n')
        else:
            print(response.json())
            print('Admin Image Upload: ', response.status_code)

    except Exception as err:
        print('Admin Image Upload Error: ', err)
