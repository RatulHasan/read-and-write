import requests

my_data = {"name": "Ratul", "email": "test@example.com"}

r = requests.post("https://www.w3schools.com/php/welcome.php", data=my_data)
# r = requests.post("https://www.w3schools.com/php/demo_form_post.php", data=my_data)

f = open("my_post.html", "w+")

f.write(r.text)
