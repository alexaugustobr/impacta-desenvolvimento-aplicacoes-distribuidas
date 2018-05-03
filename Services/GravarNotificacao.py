from Server import alunos, notificacoes
from Models.Notificacao import Notificacao
from Services.ConsultaAluno import consultaAluno

def gravarNotificacao(Notificacao):
    aluno = consultaAluno(Notificacao["aluno"])
    if not aluno:
        raise Exception("Aluno nao encontrado")
    notificacoes.append(Notificacao)
    return Notificacao