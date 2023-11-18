import requests
import json

url_credentials = 'http://web-11.challs.olicyber.it/login'

s = requests.Session()

body = {'username':'admin', 'password':'admin'}

r = s.post(url=url_credentials,json=body)

session_coockie = r.cookies

csrf_value = r.json()['csrf']

url_flag='http://web-11.challs.olicyber.it/flag_piece'

flag = ''

for i in range(4):

    r = s.get(url=(url_flag+'?csrf='+csrf_value+'&index='+str(i)),
            cookies=session_coockie)
    
    csrf_value = r.json()['csrf']

    flag_piece = r.json()['flag_piece']
    
    flag = flag + flag_piece
    
print(flag)