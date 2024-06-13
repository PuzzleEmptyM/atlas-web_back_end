#!/usr/bin/env python3
"""Change school topics"""


def update_topics(mongo_collection, name, topics):
    """
    Change all topics of school document based on name
    """
    topics_to_update = {"$set": {"topics": topics}}
    key_to_update = {"name": name}
    mongo_collection.update_many(key_to_update, topics_to_update)
