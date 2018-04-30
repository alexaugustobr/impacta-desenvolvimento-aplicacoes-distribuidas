import requests as Req

Url = "http://localhost:5000/forum/inactivate"

Forum = {"ForumId":"1", "OwnerId":"1"}
Retorno = Req.api.post(Url, json = Forum).json()

print (Retorno)