from Server import forums

def InativarForum():
    Dados = request.get_json()

    for forum in forums:
        if str(forum["ForumId"]) == str(Dados["ForumId"]) and str(forum["OwnerId"]) == str(Dados["OwnerId"]):
            if forum["Active"] == True:
                forum["Active"] = False
                return forum
    return None