from Server import alunos
from Models.Aluno import Aluno

def consultaAluno(ra):
    for aluno in alunos:
        if str(aluno["ra"]) == str(ra):
            return aluno
    return None