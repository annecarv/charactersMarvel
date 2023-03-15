import requests
import pandas as pd
from hashConfig import hash_config
import dotenv
from dotenv import load_dotenv
import os
import datetime

dotenv.load_dotenv(dotenv.find_dotenv())

time_stamp = datetime.datetime.now().strftime('%Y-%m-%d%H:%M:%S')

private_key = os.getenv('privateKey')
public_key = os.getenv('publicKey')
base_endpoint = os.getenv('baseEndpoint')

params = {
    'ts': time_stamp,
    'apikey': public_key,
    'hash': hash_config(),
    'offset': 0,
    'limit': 100
}

def get_characters():

    response_request = requests.get(base_endpoint, params=params).json()

    data_collection = []

    for item in response_request['data']['results']:
        id = item["id"]
        name = item["name"]
        description = item["description"]
        comics = item["comics"]["available"]
        series = item["series"]["available"]
        stories = item["stories"]["available"]
        events = item["events"]["available"]

        data_set = {"id": id, "name": name, "description": description, "comics": comics, "series": series, "stories": stories, "events" : events }

        data_collection.append(data_set)

        df = pd.DataFrame(data_collection, dtype=None, columns = ['id','name','description','comics','series','stories','events'])
        df.to_csv('marvelTricks.csv', index = False)

        html_view = df.to_html(justify='center')
        html_config = open("index.html", "w")
        html_config.write(html_view)
        html_config.close()

    print(df)
    print(html_view)


get_characters()
