from Server import alunos, foruns, posts
from Models.Posts import Postagem

def criarPost(Postagem):
    if not Postagem["OwnerId"] or Postagem["OwnerId"] == "":
        raise Exception("Aluno nao encontrado")

    elif not Postagem["ForumId"] or Postagem["ForumId"] == "":
        raise Exception("Forum não encontrado")

    elif not Postagem["PostId"] or Postagem["PostId"] == "":
        raise Exception("Id do Post não encontrado")

    elif not Postagem["CreateDate"] or Postagem["CreateDate"] == "":
        raise Exception("Data de criação não encontrada")

    elif not Postagem["Mensagem"] or Postagem["Mensagem"] == "":
        raise Exception("Mensagem não encontrada")

    else:
        return posts.append(Postagem)