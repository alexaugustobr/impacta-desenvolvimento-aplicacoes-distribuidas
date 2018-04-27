from Server import forums
from Services.ConsultaForum import consultarForum

def AtivarForum():
    Dados = request.get_json()

    forum = consultarForum(Dados["ForumId"])
    if forum:
        raise Exception("Forum nao encontrado")

    if str(forum["OwnerId"]) != str( Dados["OwnerId"]):
        raise Exception("OwnerId nao é o mesmo que o ownerID do Forum")
    
    if forum["Active"] == True:
        raise Exception("Forum ja esta ativo")

    forum["Active"] = True

    return forum