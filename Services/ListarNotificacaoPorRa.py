from Server import notificacoes, alunos

def listarNotificacaoPorRa(alunoRA):
    l = []
    for notificacao in notificacoes:
        if str(notificacao["aluno"]) == str(alunoRA):
            l.append(notificacao)
    return l