import requests

url="http://localhost:6800/schedule.json"
data={'project':'spamtest','spider':'spamtest0'}

print(requests.post(url=url,data=data))