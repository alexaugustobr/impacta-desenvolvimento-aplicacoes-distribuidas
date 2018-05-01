from Server import posts
from flask import jsonify

def consultaPost(PostId):

    for post in posts:
        if post['PostId'] == PostId:
            return post
    
    return None
