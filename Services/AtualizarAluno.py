from Server import alunos
from Models.Aluno import Aluno

def atualizarAluno(aluno,ra):
    for alunoNaLista in alunos:
        if str(alunoNaLista["ra"]) == str(ra):
            alunos.remove(alunoNaLista)
            alunos.append(aluno)
            return aluno
    
    return None
    