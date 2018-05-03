from Server import notificacoes, alunos

def filtrarNotificacaoPorAssunto(assunto, alunoRA):
    for notificacao in notificacoes:
        if assunto == notificacoes["assunto"] and alunoRA == notificacoes["aluno"]:
            return notificacao
        return none