import requests as Req

Url = "http://localhost/forum/inactivate"

Forum = {"ForumId":"1", "OwnerId":"Alan"}
Retorno = Req.api.post(Url, json = forum).json()

print (Retorno)