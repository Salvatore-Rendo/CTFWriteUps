import requests

url = 'http://web-08.challs.olicyber.it/login'
post = {'username':'admin', 'password':'admin'}

r = requests.post(url=url,data=post)

print(r.text)