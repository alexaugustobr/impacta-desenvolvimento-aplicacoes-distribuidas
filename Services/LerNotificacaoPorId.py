from Server import notificacoes

def lerNotificacaoPorId(notificacaoId):
    for notificacao in notificacoes:
        if str(notificacao["id"]) == str(notificacaoId):
            return notificacao
    return None