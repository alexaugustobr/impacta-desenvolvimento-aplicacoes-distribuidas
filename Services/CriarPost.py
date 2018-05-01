from Server import alunos, foruns, posts
from Models.Postagem import Postagem
from Services.ConsultaForum import consultaForum
from Services.ConsultaAluno import consultaAluno

def criarPost(Postagem):
    if not consultaAluno(Postagem["OwnerId"]):
        raise Exception("Aluno nao encontrado")

    if not consultaForum(Postagem["ForumId"]):
        raise Exception("Forum não encontrado")

    posts.append(Postagem)
    
    return Postagem