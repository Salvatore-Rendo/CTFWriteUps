import requests

url = 'http://web-09.challs.olicyber.it/login'
post = {'username':'admin', 'password':'admin'}

r = requests.post(url=url,json=post)

print(r.text)