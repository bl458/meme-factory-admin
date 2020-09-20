import json
import urllib.request


def login_admin(email, pw):
    # Log in to new admin session
    url = 'http://localhost:3000/admin/session/'
    body = {"email": email, "pw": pw}
    body = urllib.parse.urlencode(body).encode('ascii')  # body in bytes

    req = urllib.request.Request(url, body)

    try:
        res = urllib.request.urlopen(req)
        token = res.read().decode('utf-8')
        return token
    except Exception as err:
        print('Admin login error: ', err)
