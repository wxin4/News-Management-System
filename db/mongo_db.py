from pymongo import MongoClient

client = MongoClient(host = 'localhost', port = 27017)
client.admin.authenticate('admin', '@Lbq54824674')