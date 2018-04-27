from Server import foruns
from flask import jsonify

def consultarForum(ForumId):
    for forum in foruns:
        if str(forum["ForumId"]) == str(ForumId):
            return forum
    return None
