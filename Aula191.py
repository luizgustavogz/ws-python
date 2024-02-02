# requests para requisições HTTP no Python
import requests

# http:// -> Porta 80
# https:// -> Porta 443
url = 'http://localhost:3333/'
response = requests.get(url)

print(response.status_code)  # 200
# print(response.headers)
# print(response.content)
# print(response.json())
print(response.text)
