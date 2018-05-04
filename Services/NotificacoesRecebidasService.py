from Models.Notificacao import Notificacao
from Server import notificacoes

def notificacoesRecebidas(ra):
    notificacoesR = []
    for notificacao in notificacoes:
        if str(notificacao['aluno']) == str(ra) and notificacao['status'] not "Arquivado" and notificacao['status'] not 'Vizualizado':
            notificacoesR.append(notificacao)
    t = len(notificacoesR)
    
    if t > 0:
        return t

    return 0