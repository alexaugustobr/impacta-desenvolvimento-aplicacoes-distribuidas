from Server import app
from flask import jsonify, request
from Models.Resposta import Resposta

from Services.CriarForum import criarForum
from Services.InativarForum import inativarForum
from Services.AtivarForum import ativarForum
from Services.ConsultaForum import consultaForum
from Services.ListarForum import listarForum

from Services.RegistrarForum import registrarForum
from Services.RemoverRegistroForum import removerRegistroForum

@app.route("/forum", methods=["GET"])
def listarForunsAtivos():
    
    foruns = listarForum()

    if len(foruns) == 0: 
        Resposta["Status"] = "Error"
        Resposta["Dados"] = {}
        Resposta["Mensagem"] = "Sem foruns"
        return jsonify(Resposta)

    Resposta["Status"] = "Sucesso"
    Resposta["Dados"] = foruns
    Resposta["Mensagem"] = "Consulta de foruns"
    return jsonify(Resposta)


@app.route("/forum", methods=["POST"])
def criaForum():
    dados = request.get_json()

    forum = criarForum(dados)

    Resposta["Status"] = "Sucesso"
    Resposta["Dados"] = forum
    Resposta["Mensagem"] = "Forum Criado"

    return jsonify(Resposta)

@app.route("/forum/inactivate", methods=["POST"])
def inativarForumRota():
    Dados = request.get_json()
    forum = inativarForum(Dados)

    if forum:
        Resposta["Status"] = "Sucesso"
        Resposta["Dados"] = forum
        Resposta["Mensagem"] = "Forum Inativado"
        return jsonify(Resposta)

    Resposta["Status"] = "Error"
    Resposta["Dados"] = {}
    Resposta["Mensagem"] = "Forum nao encontrado"
    return jsonify(Resposta)

@app.route("/forum/activate", methods=["POST"])
def ativarForumRota():
    Dados = request.get_json()
    forum = ativarForum(Dados)

    if forum:
        Resposta["Status"] = "Sucesso"
        Resposta["Dados"] = forum
        Resposta["Mensagem"] = "Forum ativado"
        return jsonify(Resposta)

    Resposta["Status"] = "Error"
    Resposta["Dados"] = {}
    Resposta["Mensagem"] = "Forum nao encontrado"
    return jsonify(Resposta)

@app.route("/foruns/<ForumId>", methods=["GET"])
def consultarForum(ForumId):
    forum = consultaForum(ForumId)
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

@app.route("/forum/register", methods=["POST"])
def register():
    dados = request.get_json()
    Resposta["Status"] = "Sucesso"
    Resposta["Dados"] = registrarForum(dados)
    Resposta["Mensagem"] = "Aluno registrado no forum"
    return jsonify(Resposta)

@app.route("/forum/unregister", methods=["POST"])
def unregister():
    dados = request.get_json()
    Resposta["Status"] = "Sucesso"
    Resposta["Dados"] = removerRegistroForum(dados)
    Resposta["Mensagem"] = "Registro retirado do forum"
    return jsonify(Resposta)