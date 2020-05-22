import os
import json

with open('Man to love.json', encoding="utf-8") as json_file:
    data = json.load(json_file)
    for chapter in data:
        for audio in data[chapter]:
            os.rename(audio["FileName"]+'.mp3',str(audio["columnIndex"])+'_'+audio["TrackName"]+'.mp3')
            # print(audio["FileName"])
            # print(audio["TrackName"])
            # print(audio["columnIndex"])