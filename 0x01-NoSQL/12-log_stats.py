#!/usr/bin/env python3
"""
Log Stats
"""
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx
    print("{} logs".format(collection.count_documents({})))
    print("Methods:")
    print("\tmethod GET: {}".format(collection.count_documents({"method": "GET"})))
    print("\tmethod POST: {}".format(collection.count_documents({"method": "POST"})))
    print("\tmethod PUT: {}".format(collection.count_documents({"method": "PUT"})))
    print("\tmethod PATCH: {}".format(collection.count_documents({"method": "PATCH"})))
    print("\tmethod DELETE: {}".format(collection.count_documents({"method": "DELETE"})))
    print("{} status check".format(collection.count_documents({"method": "GET", "path": "/status"})))