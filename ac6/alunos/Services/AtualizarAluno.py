from Server import alunos
from Models.Aluno import Aluno

def atualizarAluno(aluno):
    print(alunos)
    print("atualizado")
    for alunoNaLista in alunos:
        if str(alunoNaLista["ra"]) == str(aluno["ra"]):
            alunos.remove(alunoNaLista)
            alunos.append(aluno)
            print(alunos)
            return aluno
    
    return None
    