#!/usr/bin/env python3
"""Log stats"""
from pymongo import MongoClient


if __name__ == '__main__':
    """
    Provides stats about Nginx logs stored in MongoDB
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    logs = db.nginx
    count_logs = logs.count_documents({})
    print(f'{count_logs} logs')
    print('Methods:')
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count_method = logs.count_documents({'method': method})
        print(f'\tmethod {method}: {count_method}')
    status = logs.count_documents({'method': 'GET', 'path': '/status'})
    print(f'{status} status check')
