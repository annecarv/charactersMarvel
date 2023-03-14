import requests
import hashlib
import datetime
import json
import pandas as pd

publicKey = 'af42d135bf129d0ef2e79e2a3abb2e92'
privateKey = '80f0e0b9547c0afa99f41963d1c10c02b16c9093'

baseEndpoint = 'https://gateway.marvel.com/v1/public/characters'

timeStamp = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')


def hashConfig():
    hashMd5 = hashlib.md5()
    hashMd5.update(f'{timeStamp}{privateKey}{publicKey}'.encode('utf-8'))
    hashConfig = hashMd5.hexdigest()

    return hashConfig


params = {
    'ts': timeStamp,
    'apikey': publicKey,
    'hash': hashConfig(),
    'limit': 100
}


def getCharacters():

    responseRequest = requests.get(baseEndpoint, params=params).json()

    dataCollection = []

    for i in responseRequest['data']['results']:
        id = i["id"]
        name = i["name"]
        description = i["description"]
        comics = i["comics"]["available"]
        series = i["series"]["available"]
        stories = i["stories"]["available"]
        events = i["events"]["available"]

        dataSet = {"id": id, "name": name, "description": description, "comics": comics, "series": series, "stories": stories, "events" : events }
        
        dataCollection.append(dataSet)

        df = pd.DataFrame(dataCollection, dtype=None, columns = ['id','name','description','comics','series','stories','events'])
        df.to_csv('marvelTricks.csv', index = False)

        htmlView = df.to_html(justify='center')
        htmlConfig = open("index.html", "w")
        htmlConfig.write(htmlView)
        htmlConfig.close()

    print(df)
    print(htmlView)


getCharacters()
