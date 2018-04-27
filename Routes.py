from Server import app
from flask import jsonify, request
from Services.AtualizarAluno import atualizarAluno
from Services.CadastrarAluno import cadastrarAluno
from Services.DeletarAluno import deletarAluno
from Services.ListarAluno import listarAlunos
from Services.ConsultarAluno import consultarAluno
<<<<<<< HEAD
from Services.CriarForum import criarForum
from Services.CriarPost import criarPost
=======
from Services.ForumInactivate import InativarForum
from Services.ForumActivate import AtivarForum
>>>>>>> 195162cccc30e2f49e996eec8c39b5cb66e9b59c
from Models.Aluno import Aluno
from Models.Resposta import Resposta
from Services.ListaPostagensForum import listaPostagensForum
from Services.consultaForum import consultarForum
from Services.ListarForum import listarforum

@app.route("/alunos", methods=["GET"])
def listarAluno():
    alunos = listarAlunos()
    if len(alunos) == 0: 
        Resposta["Status"] = "Sucesso"
        Resposta["Dados"] = []
        Resposta["Mensagem"] = "Nao ha alunos"

        return jsonify(Resposta)

    Resposta["Status"] = "Sucesso"
    Resposta["Dados"] = alunos
    Resposta["Mensagem"] = "Lista Alunos"

    return jsonify(Resposta)

@app.route("/alunos/<ra>", methods=["GET"])
def consultaAluno(ra):
    aluno = consultarAluno(ra)

    if aluno:
        Resposta["Status"] = "Sucesso"
        Resposta["Dados"] = aluno
        Resposta["Mensagem"] = "Consulta de Alunos"
        return jsonify(Resposta)

    Resposta["Status"] = "Error"
    Resposta["Dados"] = {}
    Resposta["Mensagem"] = "Aluno nao encontrado"
    return jsonify(Resposta)

@app.route("/alunos", methods=["POST"])
def cadastroAluno():
    dados = request.get_json()

    aluno = cadastrarAluno({"ra":dados["ra"], "nome":dados["nome"]})

    Resposta["Status"] = "Sucesso"
    Resposta["Dados"] = aluno
    Resposta["Mensagem"] = "Aluno Cadastrado"

    return jsonify(Resposta)

@app.route("/alunos/<ra>", methods=["PUT"])
def atualizaAluno(ra):
    dados = request.get_json()

    aluno = atualizarAluno({"ra":dados["ra"], "nome":dados["nome"]},ra)

    if aluno:
        Resposta["Status"] = "Sucesso"
        Resposta["Dados"] = aluno
        Resposta["Mensagem"] = "Aluno atualizado"
        return jsonify(Resposta)

    Resposta["Status"] = "Error"
    Resposta["Dados"] = {}
    Resposta["Mensagem"] = "Aluno nao encontrado"
    return jsonify(Resposta)

@app.route("/alunos/<ra>", methods=["DELETE"])
def removerAluno(ra):

    removido = deletarAluno(ra)

    if removido:
        Resposta["Status"] = "Sucesso"
        Resposta["Dados"] = {}
        Resposta["Mensagem"] = "Aluno Removido"
        return jsonify(Resposta)

    Resposta["Status"] = "Error"
    Resposta["Dados"] = {}
    Resposta["Mensagem"] = "Aluno nao encontrado"
    return jsonify(Resposta)


@app.route("/forum", methods=["POST"])
def criarForum():
    dados = request.get_json()

    forum = criarForum(
        {
            "ForumId":dados["ForumId"], 
            "OwnerId":dados["OwnerId"], 
            "Title": dados["Title"], 
            "Description":dados["Description"], 
            "CreateDate":dados["CreateDate"], 
            "LastPostDate":dados["LastPostDate"], 
            "Active":dados["Active"]
        }
    )

    Resposta["Status"] = "Sucesso"
    Resposta["Dados"] = forum
    Resposta["Mensagem"] = "Forum Criado"

    return jsonify(Resposta)

@app.route("/forum/post", methods=["POST"])
def criarPost():
    dados = request.get_json()
    post = criarPost(
        {
            "PostId":dados["PostId"],
            "ForumId": dados["ForumId"],
            "OwnerId":dados["OwnerId"],
            "CreateDate":dados["CreateDate"],
            "Message": dados["Message"],
            "Visible": dados["Visible"]
        }
    )

@app.route("/forum/inactivate", methods=["POST"])
def InativarForumRota():
    if forum:
        Resposta["Status"] = "Sucesso"
        Resposta["Dados"] = InativarForum()
        Resposta["Mensagem"] = "Forum Inativado"
        return jsonify(Resposta)

    Resposta["Status"] = "Error"
    Resposta["Dados"] = {}
    Resposta["Mensagem"] = "Forum nao encontrado"
    return jsonify(Resposta)

@app.route("/forum/activate", methods=["POST"])
def AtivarForumRota():
    if forum:
        Resposta["Status"] = "Sucesso"
        Resposta["Dados"] = AtivarForum()
        Resposta["Mensagem"] = "Forum ativado"
        return jsonify(Resposta)

    Resposta["Status"] = "Error"
    Resposta["Dados"] = {}
    Resposta["Mensagem"] = "Forum nao encontrado"
    return jsonify(Resposta)

@app.route("/forum/<ForumId>/post", methods=["GET"])
def listaPostagensForuns(ForumId):
    postagens = listaPostagensForum(ForumId)
    Resposta = {"Status":"","Dados":"", "Mensagem":""}

    if len(foruns) == 0: 
        Resposta["Status"] = "Sucesso"
        Resposta["Dados"] = []
        Resposta["Mensagem"] = "Nao ha foruns"

        return jsonify(Resposta)

    Resposta["Status"] = "Sucesso"
    Resposta["Dados"] = postagens
    Resposta["Mensagem"] = "Lista postagens"

    return jsonify(Resposta)

@app.route("/foruns/<ForumId>", methods=["GET"])
def consultaForum(ForumId):
    forum = consultarForum(ForumId)
    Resposta = {"Status":"","Dados":"", "Mensagem":""}

    
    if forum:
        Resposta["Status"] = "Sucesso"
        Resposta["Dados"] = forum
        Resposta["Mensagem"] = "Consulta de foruns"
        return jsonify(Resposta)

    Resposta["Status"] = "Error"
    Resposta["Dados"] = {}
    Resposta["Mensagem"] = "forum nao encontrado"
    return jsonify(Resposta)

@app.route("/forum", methods=["GET"])
def listarForunsAtivos():
    foruns = listarforum()

    if Forumid
        Resposta["Status"] = "Sucesso"
        Resposta["Dados"] = foruns
        Resposta["Mensagem"] = "Consulta de Forum"
        return jsonify(Resposta)

    Resposta["Status"] = "Error"
    Resposta["Dados"] = {}
    Resposta["Mensagem"] = "Sem foruns"
    return jsonify(Resposta)
