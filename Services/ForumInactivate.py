from Server import forums
from Services.ConsultaForum import consultarForum
from flask import request

def InativarForum():
    Dados = request.get_json()

    forum = consultarForum(Dados["ForumId"])
    if forum:
        raise Exception("Forum nao encontrado")

    if str(forum["OwnerId"]) != str( Dados["OwnerId"]):
        raise Exception("OwnerId nao é o mesmo que o ownerID do Forum")
    
    if forum["Active"] == False:
        raise Exception("Forum ja esta inativo")

    forum["Active"] = False

    return forum