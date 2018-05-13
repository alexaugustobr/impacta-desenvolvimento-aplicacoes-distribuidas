from Server import mensagens
from Models.Mensagem import Mensagem

def consultaMensagem(id):
    for mensagem in mensagens:
        if str(mensagem["id"]) == str(id):
            return mensagem
    return None