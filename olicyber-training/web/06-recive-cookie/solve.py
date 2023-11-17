import requests

url_token = 'http://web-06.challs.olicyber.it/token'
url_flag = 'http://web-06.challs.olicyber.it/flag'

s = requests.session()

s.get(url=url_token)

r = s.get(url=url_flag)

print(r.text)