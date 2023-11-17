import requests

url = 'http://web-07.challs.olicyber.it/'

r = requests.head(url=url)

print(r.headers)