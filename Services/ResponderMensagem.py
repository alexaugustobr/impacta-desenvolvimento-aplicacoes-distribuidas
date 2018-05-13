from Server import mensagens
from Models.Mensagem import Mensagem
from Services.CadastrarMensagem import cadastrarMensagem

def responderMensagem(id, resposta):

    for mensagem in mensagens:
        if str(mensagem["id"]) == str(id):
            resposta = cadastrarMensagem(resposta)
            mensagem['respostas'].append(resposta["id"])
            return resposta
    
    return None