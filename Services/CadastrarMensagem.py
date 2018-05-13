from Server import mensagens
from Models.Mensagem import Mensagem
from Services.ConsultaMensagem import consultaMensagem

def cadastrarMensagem(mensagem):
    if consultaMensagem(mensagem["id"]):
        raise Exception("Mensagem existe com esse id")
    mensagens.append(mensagem)
    return mensagem