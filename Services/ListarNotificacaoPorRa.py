from Server import notificacoes, alunos

def listarNotificacaoPorRa(alunoRA):
    if alunoRA in alunos:
        for notificacao in notificacoes:
            if notificacoes["aluno"] == alunoRA:
                return notificacao
    return None