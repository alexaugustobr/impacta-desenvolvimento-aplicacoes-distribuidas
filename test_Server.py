from flask import request, jsonify
from Server import app

import pytest

#CRIAR ALUNO
with app.test_client() as c:
    aluno = {'ra': '1700072', 'nome': 'alex'}
    rv = c.post('/alunos', json=aluno)
    json_data = rv.get_json()
    assert aluno == json_data['Dados']

with app.test_client() as c:
    aluno = {'ra': '1700073', 'nome': 'dani'}
    rv = c.post('/alunos', json=aluno)
    json_data = rv.get_json()
    assert aluno == json_data['Dados']


#LISTAR ALUNO
with app.test_client() as c:
    aluno1 = {'ra': '1700072', 'nome': 'alex'}
    aluno2 = {'ra': '1700073', 'nome': 'dani'}
    alunos = [aluno1,aluno2]
    rv = c.get('/alunos')
    json_data = rv.get_json()
    assert alunos == json_data['Dados']
#criar forum
with app.test_client() as c:
    forum = {"ForumId":"1", "OwnerId":"1700072", "Title": "Title", "Description":"Description", "CreateDate":"10/10/2017", "LastPostDate":"10/10/2017", "Active":True}
    rv = c.post('/forum', json=forum)
    json_data = rv.get_json()
    assert forum == json_data['Dados']
#LISTAR forum
with app.test_client() as c:
    forum = {"ForumId":"1", "OwnerId":"1700072", "Title": "Title", "Description":"Description", "CreateDate":"10/10/2017", "LastPostDate":"10/10/2017", "Active":True}
    f = [forum]
    rv = c.get('/forum')
    json_data = rv.get_json()
    assert f == json_data['Dados']

#register forum
with app.test_client() as c:
    r = {"ForumId":"1", "ra":"1700072"}
    rv = c.post('/forum/register', json=r)
    json_data = rv.get_json()
    assert True == json_data['Dados']

#registrar
with app.test_client() as c:
    r = {"ForumId":"1", "ra":"1700073"}
    rv = c.post('/forum/register', json=r)
    json_data = rv.get_json()
    assert True == json_data['Dados']
#unregister
with app.test_client() as c:
    r = {"ForumId":"1", "ra":"1700073"}
    rv = c.post('/forum/unregister', json=r)
    json_data = rv.get_json()
    assert True == json_data['Dados']
#criar post
with app.test_client() as c:
	Postagem = {"PostId":"1", "ForumId": "1", "OwnerId":"1700072", "CreateDate":"10/10/2017", "Message": "Teste", "Visible":True}
	rv = c.post('/forum/post', json=Postagem)
	json_data = rv.get_json()
	assert Postagem == json_data['Dados']
#ler post
with app.test_client() as c:
	Postagem = {"PostId":"1", "ForumId": "1", "OwnerId":"1700072", "CreateDate":"10/10/2017", "Message": "Teste", "Visible":True}
	rv = c.get('/forum/post/1?ra=1700072')
	json_data = rv.get_json()
	assert Postagem == json_data['Dados']

#CRIAR professor
with app.test_client() as c:
    professor = {'ra': '123456', 'nome': 'professor'}
    rv = c.post('/professores', json=professor)
    json_data = rv.get_json()
    assert professor == json_data['Dados']


#CRIAR mensagem
with app.test_client() as c:
    mensagem = {
            "id":"33",
            "texto":"Olá nova AC disponivel",
            "destinatario":"1700072",
            "remetente":"123456",
            "lida":False,
            "arquivada":False,
            "respostas":[]
        }
    rv = c.post('/mensagens', json=mensagem)
    json_data = rv.get_json()
    assert mensagem == json_data['Dados']



#ler mensagem
with app.test_client() as c:
    rv = c.get('/mensagens/33/ler')
    json_data = rv.get_json()
    assert True == json_data['Dados']


#arquivar mensagem
with app.test_client() as c:
    rv = c.get('/mensagens/33/arquivar')
    json_data = rv.get_json()
    assert True == json_data['Dados']


#responder mensagem
with app.test_client() as c:
    mensagem = {
            "id":"34",
            "texto":"Ac feita",
            "destinatario":"123456",
            "remetente":"1700072",
            "lida":False,
            "arquivada":False,
            "respostas":[]
        }
    rv = c.post('/mensagens/33/responder', json=mensagem)
    json_data = rv.get_json()
    assert mensagem == json_data['Dados']











