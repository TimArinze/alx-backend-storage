#!/usr/bin/env python3
"""
Top students
"""


def top_students(mongo_collection):
    """function that returns all students sorted by average score"""
    result = mongo_collection.aggregate([
             {
                 "$group": {
                     "name": {"$sort": "$score"},
                     "averageScore": {"$avg": "$score"}
                     }
                 }
             ]
             )
    return result
