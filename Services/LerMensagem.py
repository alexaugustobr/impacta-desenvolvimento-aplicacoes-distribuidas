from Server import mensagens
from Models.Mensagem import Mensagem

def lerMensagem(id):
    for mensagem in mensagens:
        if str(mensagem["id"]) == str(id):
            mensagem["lida"] = True
            return True
    return False