import requests
from io import BytesIO
from PIL import Image

# r = requests.get("https://images8.alphacoders.com/815/815404.jpg")
r = requests.get("https://i.pinimg.com/originals/d3/f0/eb/d3f0ebdf9705f2b9eefdcb0d7df99b76.jpg")

print("Status", r.status_code)

image = Image.open(BytesIO(r.content))

print(image.size, image.format, image.mode)

path = "./image." + image.format

try:
    image.save(path, image.format)

except IOError:
    print("Can\'t save image!")