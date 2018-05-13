from Server import mensagens
from Models.Mensagem import Mensagem

def arquivarMensagem(id):
    for mensagem in mensagens:
        if str(mensagem["id"]) == str(id):
            mensagem["arquivada"] = True
            return True
    return False