from Server import notificacoes, alunos
from Services.lerNotificacaoPorId import lerNotificacaoPorId
from Services.lerNotificacaoPorRa import lerNotificacaoPorRa


def excluiNotificacao(id, ra):

    for notificacaoNaLista in notificacoes and alunoNaLista in alunos:
        if notificacaoNaLista['id'] == id and alunoNaLista['ra'] == ra:
            notificacoes.remove(notificacaoNaLista)
            return True
    return False
