import requests
import pandas as pd
from hashConfig import hashConfig
import dotenv
from dotenv import load_dotenv
import os
import datetime

dotenv.load_dotenv(dotenv.find_dotenv())

timeStamp = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')

privateKey = os.getenv('privateKey')
publicKey = os.getenv('publicKey')
baseEndpoint = os.getenv('baseEndpoint')

params = {
    'ts': timeStamp,
    'apikey': publicKey,
    'hash': hashConfig(),
    'offset': 1,
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
