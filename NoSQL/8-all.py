#!/usr/bin/env python3
"""List all documents in Python"""


def list_all(mongo_collection):
    """
    Write Python function that lists all documents in collection
    """
    return list(mongo_collection.find())
