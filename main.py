import requests
import datetime
import json
import pandas as pd
import hashConfig

publicKey = 'af42d135bf129d0ef2e79e2a3abb2e92'
privateKey = '80f0e0b9547c0afa99f41963d1c10c02b16c9093'

baseEndpoint = 'https://gateway.marvel.com/v1/public/characters'

timeStamp = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')

params = {
    'ts': timeStamp,
    'apikey': publicKey,
    'hash': hashConfig(),
    'limit': 100
}


def getCharacters():

    responseRequest = requests.get(baseEndpoint, params=params).json()

    dataCollection = []

    for item in responseRequest['data']['results']:
        id = item["id"]
        name = item["name"]
        description = item["description"]
        comics = item["comics"]["available"]
        series = item["series"]["available"]
        stories = item["stories"]["available"]
        events = item["events"]["available"]

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
