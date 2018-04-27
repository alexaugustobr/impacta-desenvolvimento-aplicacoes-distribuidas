from Server import forums

def AtivarForum():
    Dados = request.get_json()

    for forum in forums:
        if str(forum["ForumId"]) == str(Dados["ForumId"]) and str(forum["OwnerId"]) == str(Dados["OwnerId"]):
            if forum["Active"] == False:
                forum["Active"] = True
                return forum
    return None