import requests
res = requests.get('https://myip.ipip.net').text
print(res)

