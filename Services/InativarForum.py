from Server import foruns
from Services.ConsultaForum import consultaForum


def inativarForum(Dados):
    

    forum = consultaForum(Dados["ForumId"])
    if forum:
        raise Exception("Forum nao encontrado")

    if str(forum["OwnerId"]) != str( Dados["OwnerId"]):
        raise Exception("OwnerId nao é o mesmo que o ownerID do Forum")
    
    if forum["Active"] == False:
        raise Exception("Forum ja esta inativo")

    forum["Active"] = False

    return forum