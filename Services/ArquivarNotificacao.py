from Server import notificacoes
from Models.Notificacao import Notificacao
from Services.LerNotificacaoPorId import lerNotificacaoPorRa
from Services.LerNotificacaoPorRa import lerNotificacaoPorRa

def arquivarNotificacao(ra, id){
    arquivarId = lerNotificacaoPorId(id)
    arquivarRa = lerNotificacaoPorRa(ra)

    if arquivarRa and arquivarId:
        notificacoes["status"] = "Arquivada"

        return notificacoes
            
    return None

}