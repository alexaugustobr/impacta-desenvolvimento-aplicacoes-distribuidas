from Server import professores
from Models.Professor import Professor
from Services.ConsultaProfessor import consultaProfessor

def cadastrarProfessor(professor):
    if consultaProfessor(professor["ra"]):
        raise Exception("Mensagem existe com esse ra")
    professores.append(professor)
    return professor