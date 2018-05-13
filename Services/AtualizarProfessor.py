from Server import professores
from Models.Professor import Professor

def atualizarProfessor(professor,ra):
    for professorNaLista in professores:
        if str(professorNaLista["ra"]) == str(ra):
            professores.remove(professorNaLista)
            professores.append(professor)
            return professor
    
    return None
    