from Server import alunos
from Models.Aluno import Aluno

def consultarAluno(ra):
    for aluno in alunos:
        if str(aluno["ra"]) == str(ra):
            return aluno
    return None