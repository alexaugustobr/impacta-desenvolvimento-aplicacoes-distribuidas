from Server import app
from flask import jsonify, request
from Models.Resposta import Resposta

from Services.CadastrarMensagem import cadastrarMensagem
from Services.ListarMensagem import listarMensagem
from Services.ConsultaMensagem import consultaMensagem
from Services.LerMensagem import lerMensagem
from Services.ArquivarMensagem import arquivarMensagem
from Services.ExcluirMensagem import excluirMensagem
from Services.ResponderMensagem import responderMensagem

@app.route("/mensagens", methods=["GET"])
def listarMensagem():
    dados = request.args
    mensagens = listarMensagem(dados['ra'])
    if len(mensagens) == 0: 
        Resposta["Status"] = "Sucesso"
        Resposta["Dados"] = []
        Resposta["Mensagem"] = "Nao ha mensagens"

        return jsonify(Resposta)

    Resposta["Status"] = "Sucesso"
    Resposta["Dados"] = mensagens
    Resposta["Mensagem"] = "Lista Mensagens"

    return jsonify(Resposta)

@app.route("/mensagens/<id>", methods=["GET"])
def consultarMensagem(id):
    mensagem = consultaMensagem(id)

    if mensagem:
        Resposta["Status"] = "Sucesso"
        Resposta["Dados"] = mensagem
        Resposta["Mensagem"] = "Consulta de Mensagens"
        return jsonify(Resposta)

    Resposta["Status"] = "Error"
    Resposta["Dados"] = {}
    Resposta["Mensagem"] = "Mensagem nao encontrado"
    return jsonify(Resposta)

@app.route("/mensagens", methods=["POST"])
def cadastroMensagem():
    dados = request.get_json()

    mensagem = cadastrarMensagem(dados)

    Resposta["Status"] = "Sucesso"
    Resposta["Dados"] = mensagem
    Resposta["Mensagem"] = "Mensagem Cadastrado"

    return jsonify(Resposta)

@app.route("/mensagens/<id>/ler", methods=["GET"])
def leituraMensagem(id):
    mensagem = lerMensagem(id)

    if mensagem:
        Resposta["Status"] = "Sucesso"
        Resposta["Dados"] = mensagem
        Resposta["Mensagem"] = "Lida Mensagem"
        return jsonify(Resposta)

    Resposta["Status"] = "Error"
    Resposta["Dados"] = {}
    Resposta["Mensagem"] = "Mensagem nao encontrado"
    return jsonify(Resposta)

@app.route("/mensagens/<id>/arquivar", methods=["GET"])
def arquivaMensagem(id):
    mensagem = arquivarMensagem(id)

    if mensagem:
        Resposta["Status"] = "Sucesso"
        Resposta["Dados"] = mensagem
        Resposta["Mensagem"] = "Arquivada Mensagem"
        return jsonify(Resposta)

    Resposta["Status"] = "Error"
    Resposta["Dados"] = {}
    Resposta["Mensagem"] = "Mensagem nao encontrado"
    return jsonify(Resposta)

@app.route("/mensagens/<id>", methods=["DELETE"])
def excluiMensagem(id):
    mensagem = excluirMensagem(id)

    if mensagem:
        Resposta["Status"] = "Sucesso"
        Resposta["Dados"] = mensagem
        Resposta["Mensagem"] = "Excluido Mensagem"
        return jsonify(Resposta)

    Resposta["Status"] = "Error"
    Resposta["Dados"] = {}
    Resposta["Mensagem"] = "Mensagem nao encontrado"
    return jsonify(Resposta)


@app.route("/mensagens/<id>/responder", methods=["POST"])
def respondaMensagem(id):
    dados = request.get_json()

    mensagem = responderMensagem(id, dados)

    Resposta["Status"] = "Sucesso"
    Resposta["Dados"] = mensagem
    Resposta["Mensagem"] = "Mensagem Respondida"

    return jsonify(Resposta)