from Server import notificacoes, alunos
from Models import Notificacao

def lerNotificacaoPorRa(alunoRA):
    if alunoRA in alunos:
        for notificacao in notificacoes:
            if notificacoes["aluno"] == alunoRA:
                return notificacao
    return None