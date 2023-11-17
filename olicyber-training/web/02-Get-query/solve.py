import requests

query = {'id' : 'flag'}

r = requests.get(url='http://web-02.challs.olicyber.it/server-records',
                 params=query)

print(r.text)