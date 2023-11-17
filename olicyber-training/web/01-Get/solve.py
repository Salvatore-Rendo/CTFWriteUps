import requests

r = requests.get(url='http://web-01.challs.olicyber.it/')

print(r.text)