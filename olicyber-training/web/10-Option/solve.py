import requests

url = ' http://web-10.challs.olicyber.it/'

#r = requests.options(url=url)
r = requests.put(url=url)

print(r.headers)