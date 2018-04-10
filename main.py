import json
import os

if os.path.isfile("./ages.json") and os.stat("./ages.json").st_size != 0:

    old_file = open("ages.json", "r+")

    data = json.loads(old_file.read())

    print("Current age is "+ str(data["age"]) + "--- adding a year.")

    data["age"] +=1

    print("New age is "+ str(data["age"]))

else:
    old_file = open("ages.json", "w+")

    data = {"name": "Ratul", "age": 28}

    print("No file found! Creating new file")


old_file.seek(0)

old_file.write(json.dumps(data))








'''
newFile = open("ages.json", "w+")

string = "This is the text that will be written in the txt file!"

newFile.write(string)

'''