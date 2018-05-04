from Server import notificacoes
from Services.LerNotificacaoPorId import lerNotificacaoPorId
from Services.ConsultaAluno import consultaAluno


def excluiNotificacao(id, ra):
    aluno = consultaAluno(ra)
    notificacao = lerNotificacaoPorId(id)
    
    if not aluno:
        raise Exception("Aluno não encontrada")

    if not notificacao:
        raise Exception("Notificacao não encontrada")

    notificacoes.remove(notificacao)
    return True
    
