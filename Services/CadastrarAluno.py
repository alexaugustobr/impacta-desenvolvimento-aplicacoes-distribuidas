from Server import alunos
from Models.Aluno import Aluno
from Services.ConsultaAluno import consultaAluno

def cadastrarAluno(aluno):
    if consultaAluno(aluno["ra"]):
        raise Exception("Aluno existe com esse RA")
    alunos.append(aluno)
    return aluno