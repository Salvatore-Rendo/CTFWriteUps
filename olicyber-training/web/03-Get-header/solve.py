import requests

header = {'X-Password' : 'admin'}

url = 'http://web-03.challs.olicyber.it/flag'

r = requests.get(url=url,headers=header)

print(r.text)