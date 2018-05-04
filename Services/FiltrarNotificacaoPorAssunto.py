from Server import notificacoes, alunos

def filtrarNotificacaoPorAssunto(assunto, alunoRA):
    listaDeNotificacoes = []
    for notificacao in notificacoes:
        if assunto == notificacoes["assunto"] and alunoRA == notificacoes["aluno"]:
            listaDeNotificacoes.append(notificacao)
    return listaDeNotificacoes