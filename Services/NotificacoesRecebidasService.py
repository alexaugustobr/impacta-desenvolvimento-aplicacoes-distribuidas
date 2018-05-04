from Models.Notificacao import Notificacao
from Server import notificacoes

def notificacoesRecebidas(ra):
    notificacoesR = []
    for notificacao in notificacoes:
        if str(notificacao['aluno']) == str(ra) and notificacao['status'] != "Arquivado" and notificacao['status'] != 'Vizualizado':
            notificacoesR.append(notificacao)
    t = len(notificacoesR)
    
    if t > 0:
        return {"quantidade":t}

    return {"quantidade":0}