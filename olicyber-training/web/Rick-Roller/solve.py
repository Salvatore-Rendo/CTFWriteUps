import requests

r = requests.get(url='http://roller.challs.olicyber.it/get_flag.php',allow_redirects=False)

print(r.content)

# or curl http://roller.challs.olicyber.it/get_flag.php


