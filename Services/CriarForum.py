from Server import alunos, foruns, post
from Models.Forum import Forum
from Models.Aluno import Aluno

def criarForum(Forum):
    foruns.append(Forum)
    return Forums