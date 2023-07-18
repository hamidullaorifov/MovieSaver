import requests
import pymongo
import os
from dotenv import load_dotenv

load_dotenv()


MONGODB_USERNAME = os.getenv('MONGODB_USERNAME')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')
MONGODB_URL = os.getenv('MONGODB_URL')


SERVER_URL = os.getenv('SERVER_URL')


def save_file(file):
    with file.open(mode='rb') as f:
        response = requests.post(SERVER_URL,files={'file':f})
        file_url = ''
        if response.ok:
            data = response.json()
            file_url = data.get('file_url')
        print("Fileurl :",file_url)
        return file_url
    

client = pymongo.MongoClient(MONGODB_URL)
db = client["movies"]
collection = db["movies"]

def save_data_mongodb(data):
    item = collection.insert_one(data) 
    id_ = item.inserted_id
    return id_