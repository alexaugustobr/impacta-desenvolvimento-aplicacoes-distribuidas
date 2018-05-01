from Server import foruns
from flask import jsonify

def consultaForum(ForumId):
  for forum in foruns:
    if str(forum["ForumId"]) == str(ForumId):
      return forum
  return None
