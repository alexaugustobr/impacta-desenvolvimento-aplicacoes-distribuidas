from Server import notificacoes
from Services.LerNotificacaoPorId import lerNotificacaoPorId
from Services.ConsultaAluno import consultaAluno
from Models.Notificacao import Notificacao


def arquivarNotificacao(id, ra):
    aluno = consultaAluno(ra)
    notifica = lerNotificacaoPorId(id)
    
    if not aluno:
        raise Exception("Aluno não encontrada")

    if not notificacao:
        raise Exception("Notificacao não encontrada")
    
    for notificacao in notificacoes:
        if notificacao['id'] == notifica['id']:
            if notificacoes['status'] == "Arquivado":
                raise Exception("Notificacao já está Arquivada")
            notificacao['status'] = "Arquivado"
            return notificacoes
    return None
