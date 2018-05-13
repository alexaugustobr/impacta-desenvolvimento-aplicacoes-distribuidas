from Server import mensagens
from Models.Mensagem import Mensagem

def excluirMensagem(id):
    for mensagem in mensagens:
        if str(mensagem["id"]) == str(id):
            mensagens.remove(mensagem)
            return True
    return False