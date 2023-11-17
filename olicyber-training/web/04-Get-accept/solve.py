import requests

header = {'accept' : 'application/xml'}

url = 'http://web-04.challs.olicyber.it/users'

r = requests.get(url=url,headers=header)

print(r.text)