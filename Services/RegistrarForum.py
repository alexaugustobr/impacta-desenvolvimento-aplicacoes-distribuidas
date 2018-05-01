from Server import alunos, foruns, posts
from Models.Forum import Forum
from Services.ConsultaAluno import consultaAluno
from Services.ConsultaForum import consultaForum

def registrarForum(dados):
  
  aluno = consultaAluno(dados["ra"])
  forum = consultaForum(dados["ForumId"]) 

  if not aluno:
    raise Exception("Aluno nao encontrado.")

  if not forum:
    raise Exception("Forum nao encontrado.")
  
  if not 'foruns' in aluno.keys():
    aluno['foruns'] = []

  if not 'alunos' in forum.keys():
    forum['alunos'] = []

  if dados["ra"] in forum['alunos']:
    raise Exception("Aluno ja esta no forum.")

  if dados["ForumId"] in aluno['foruns']:
    raise Exception("Aluno ja esta no forum.")

  forum['alunos'].append(dados["ra"])
  aluno['foruns'].append(dados["ForumId"])

  return True