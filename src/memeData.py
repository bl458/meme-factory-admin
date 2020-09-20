import json
import urllib.request


url = 'http://localhost:3000/admin/session/'
body = {"email": "byungchan9707@gmail.com", "pw": "test1234"}


data = urllib.parse.urlencode(body)
data = data.encode('ascii')  # data should be bytes
req = urllib.request.Request(url, data)

try:
    res = urllib.request.urlopen(req)
    print(res.read().decode('utf-8'))
except Exception as err:
    print('Admin login error: ', err)
