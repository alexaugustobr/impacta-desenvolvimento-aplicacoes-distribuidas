from Server import notificacoes

def lerNotificacaoPorId(notificacaoId):
    for notificacao in notificacoes:
        if notificacoes["id"] == notificacoesId:
            return notificacao
    return None