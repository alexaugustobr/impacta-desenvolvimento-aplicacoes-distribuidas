from Server import alunos, foruns, posts
from Models.Postagem import Postagem
from Services.ConsultaForum import consultaForum
from Services.ConsultaAluno import consultaAluno

def criarPost(Postagem):
    aluno = consultaAluno(Postagem["OwnerId"])
    if not aluno:
        raise Exception("Aluno nao encontrado")

    forum = consultaForum(Postagem["ForumId"])
    if not forum:
        raise Exception("Forum não encontrado")

    if not 'foruns' in aluno.keys():
        aluno['foruns'] = []

    if not 'alunos' in forum.keys():
        forum['alunos'] = []

    if Postagem["OwnerId"] not in forum['alunos']:
        raise Exception("Aluno nao esta no forum.")

    if Postagem["ForumId"] not in aluno['foruns']:
        raise Exception("Aluno nao esta no forum.")

    posts.append(Postagem)
    
    return Postagem