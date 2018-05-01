from Server import alunos, foruns, posts
from Models.Forum import Forum
from Services.ConsultaAluno import consultaAluno

def criarForum(Forum):
    aluno = consultaAluno(Forum["OwnerId"])
    if not aluno:
        raise Exception("Aluno nao encontrado")
    foruns.append(Forum)
    return Forum