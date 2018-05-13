from Server import mensagens
from Models.Mensagem import Mensagem

def listarMensagem(ra):
    mensagensFiltradas = []
    for mensagem in mensagens:
        if str(mensagem["destinatario"]) == str(ra):
            mensagensFiltradas.append(mensagem)
    return mensagensFiltradas