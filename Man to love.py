import os
import json

### If you want alphabetic numbering use this code ###

first = ['a','b','c','d','e','f','g','h','i','j']
second = ['a','b','c','d','e','f','g','h','i','j']
combined = []

for letter1 in first:
    for letter2 in second:
        combined.append(letter1+letter2)

with open('Man to love.json', encoding="utf-8") as json_file:
    data = json.load(json_file)
    for chapter in data:
        for audio in data[chapter]:
            index = audio["columnIndex"]
            os.rename(audio["FileName"]+'.mp3',combined[index]+' '+audio["TrackName"]+'.mp3')
            # print(audio["FileName"])
            # print(audio["TrackName"])
            # print(audio["columnIndex"])
            
            
### If you want numeric numbering use this code ###
'''
with open('Man to love.json', encoding="utf-8") as json_file:
    data = json.load(json_file)
    for chapter in data:
        for audio in data[chapter]:
            os.rename(audio["FileName"]+'.mp3',str(audio["columnIndex"])+' '+audio["TrackName"]+'.mp3')
            # print(audio["FileName"])
            # print(audio["TrackName"])
            # print(audio["columnIndex"])
'''
