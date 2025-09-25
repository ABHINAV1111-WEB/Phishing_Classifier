import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

def get_mongo_client():
    uri= os.getenv("MONGO_URI")
    return MongoClient(uri)

def insert_dataframe(df, db_name, collection_name):
    client= get_mongo_client()
    db= client[db_name]
    collection = db[collection_name]
    collection.insert_many(df.to_dict("records"))
    print(f"✅ Inserted {len(df)} records into {db_name}.{collection_name}")