from Server import posts
from flask import jsonify
from Services.ConsultaForum import consultaForum

def listaPostagensForum(ForumId, AlunoRA):
    postagensDesseForum = []

    for post in posts:
        if post['ForumId'] == ForumId:
            postagensDesseForum.append(post)

    for post in postagensDesseForum:
        forum = consultaForum(post['ForumId'])

        if not forum:
            raise Exception("Forum nao encontrado")

        if not 'alunos' in forum.keys():
            forum['alunos'] = []

        if AlunoRA not in forum['alunos']:
            raise Exception("Aluno nao esta no forum.")

    return postagensDesseForum
