from Models.Forum import Forum
from Server import foruns

def listarforum():
    forunsAtivos = []

    for forum in foruns:
        if forum["Active"]:
            forunsAtivos.append(forum)

    return forunsAtivos

