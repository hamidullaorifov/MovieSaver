import requests
import pymongo
import os
from dotenv import load_dotenv

load_dotenv()


MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')
MONGODB_URL = f'mongodb+srv://{MONGODB_USERNAME}:{MONGODB_PASSWORD}@clusterfileurls.vkkzokc.mongodb.net/?retryWrites=true&w=majority'

SERVER_URL = os.getenv('SERVER_URL')


def save_file(file):
    with file.open(mode='rb') as f:
        response = requests.post(SERVER_URL,files={'file':f})
        file_url = ''
        if response.ok:
            data = response.json()
            file_url = data.get('file_url')
        return file_url


def save_data_mongodb(data):
    client = pymongo.MongoClient(MONGODB_URL)
    db = client["movies"]
    collection = db["movies"]
    item = collection.insert_one(data) 
    id_ = item.inserted_id

    return id_