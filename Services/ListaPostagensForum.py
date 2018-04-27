from Server import posts
from flask import jsonify

def listaPostagensForum(ForumId):
    postagensDesseForum = []
    #verificar se ForumId existe

    for post in posts:
        if post['ForumId'] == ForumId:
            postagensDesseForum.append(post)

    return postagensDesseForum
