#!/usr/bin/env python3
"""Log stats script"""
from pymongo import MongoClient

def log_stats():
    """
    Connects to MongoDB, retrieves Nginx log stats, and prints them.
    """
    client = MongoClient()
    db = client.logs
    collection = db.nginx
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    status_check = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")

if __name__ == "__main__":
    log_stats()
