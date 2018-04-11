import requests
import json

url ="https://www.googleapis.com/urlshortener/v1/url"
payload = {"longUrl": "https://acousticabd.com"}
headers = {"Content-Type": "application/json"}

r = requests.post(url, json = payload, headers = headers)

print(r.text)

f = open("url_shorten.html", "w+")
f.write(r.text)