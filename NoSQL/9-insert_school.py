#!/usr/bin/env python3
"""Insert doc in Python"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts new document in collection based on kwargs:
    """
    creation = mongo_collection.insert_one(kwargs)
    return creation.inserted_id
