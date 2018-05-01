from Server import app
from flask import jsonify, request
from Models.Resposta import Resposta

from Services.CriarPost import criarPost
from Services.ConsultaPost import consultaPost
from Services.ListaPostagensForum import listaPostagensForum

@app.route("/forum/post", methods=["POST"])
def criaPost():
    dados = request.get_json()
    post = criarPost(dados)
    Resposta["Status"] = "Sucesso"
    Resposta["Dados"] = post
    Resposta["Mensagem"] = "Post criado"
    return jsonify(Resposta)

@app.route("/forum/<ForumId>/post", methods=["GET"])
def listaPostagensForuns(ForumId):
    dados = request.args
    postagens = listaPostagensForum(ForumId,dados['ra'])
    Resposta = {"Status":"","Dados":"", "Mensagem":""}

    if len(postagens) == 0: 
        Resposta["Status"] = "Sucesso"
        Resposta["Dados"] = []
        Resposta["Mensagem"] = "Nao ha postagens no forum"

        return jsonify(Resposta)

    Resposta["Status"] = "Sucesso"
    Resposta["Dados"] = postagens
    Resposta["Mensagem"] = "Lista postagens"

    return jsonify(Resposta)


@app.route("/forum/post/<PostId>", methods=["GET"])
def consultarPost(PostId):
    dados = request.args
    post = consultaPost(PostId,dados['ra'])

    if post:
        Resposta["Status"] = "Sucesso"
        Resposta["Dados"] = post
        Resposta["Mensagem"] = "Consulta de post"
        return jsonify(Resposta)

    Resposta["Status"] = "Error"
    Resposta["Dados"] = {}
    Resposta["Mensagem"] = "Post nao encontrado"
    return jsonify(Resposta)

