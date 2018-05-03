from Server import notificacoes
from Models.Notificacao import Notificacao

def arquivarNotificacao(){
    for notificacao in notificacoes:
        if notificacao["status"] == "Nao vizualizado":
            notificacao["status"] = "Vizualizado"
    
    return notificacao

}