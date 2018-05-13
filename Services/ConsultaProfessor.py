from Server import professores
from Models.Professor import Professor

def consultaProfessor(ra):
    for professor in professores:
        if str(professor["ra"]) == str(ra):
            return professor
    return None