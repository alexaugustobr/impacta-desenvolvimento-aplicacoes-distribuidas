from Models.Forum import Forum
from Server import foruns

def listarForum():
    forunsAtivos = []

    for forum in foruns:
        if forum["Active"]:
            forunsAtivos.append(forum)

    return forunsAtivos

