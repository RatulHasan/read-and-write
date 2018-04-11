import requests
import json

url ="https://jsonplaceholder.typicode.com/posts"
payload = {"longUrl": "https://acousticabd.com"}
headers = {"Content-Type": "application/json"}

r = requests.get(url)

print(r.text)

f = open("get_dummy_json.html", "w+")
f.write(r.text)