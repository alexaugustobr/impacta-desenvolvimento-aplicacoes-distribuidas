from Server import forums

def AtivarForum(ForumId):
    for forum in forums:
        if str(forum["ForumId"]) == str(ForumId):
            if str(forum["Active"]) == False:
                forum["Active"] = True:
                return forum
    return None