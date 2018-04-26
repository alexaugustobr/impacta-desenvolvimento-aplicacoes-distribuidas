from Server import alunos
from Models.Aluno import Aluno

def deletarAluno(ra):
    for alunoNaLista in alunos:
        if str(alunoNaLista["ra"]) == str(ra):
            alunos.remove(alunoNaLista)
            return True
    return False
    