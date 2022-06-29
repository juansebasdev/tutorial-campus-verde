from pymongo import MongoClient
from config.index import config

# Connect to the MongoDB server
db_client = MongoClient(config['MONGO_URI']) 
# Create the database
db_name = db_client['demo']
# Create the collection 
db_collection = db_name['electricMeter']