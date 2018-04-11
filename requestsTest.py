import requests
from io import BytesIO
from PIL import Image

params = {"q": "ratul hasan"}

r = requests.get("https://www.bing.com/search", params=params)

print("Status: ", r.status_code)

print(r.url)

f = open("page1.html", "w+")

f.write(r.text)
f.close()