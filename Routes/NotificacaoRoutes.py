from Server import app
from flask import jsonify, request
from Models.Notificacao import Notificacao



@app.route("/notificacoes", methods=["GET"])
def listarNotificacoes():
    
    notificacoes = listarNotificacoes()

    if len(notificacoes) == 0: 
        Resposta["Status"] = "Error"
        Resposta["Dados"] = {}
        Resposta["Mensagem"] = "Nenhuma notificacao"
        return jsonify(Resposta)

    Resposta["Status"] = "Sucesso"
    Resposta["Dados"] = notificacoes
    Resposta["Mensagem"] = "VIsualizar notificaçoes"
    return jsonify(Resposta)


@app.route("/notificacoes/arquivar", methods=["POST"])
def arquivarNotificacao():
    Dados = request.get_json()
    notificacao = arquivarNotificacao(Dados)

    if notificacao:
        Resposta["Status"] = "Sucesso"
        Resposta["Dados"] = notificacao
        Resposta["Mensagem"] = "Notificacao arquivada"
        return jsonify(Resposta)

    Resposta["Status"] = "Error"
    Resposta["Dados"] = {}
    Resposta["Mensagem"] = "Notificacao nao arquivada"
    return jsonify(Resposta)



@app.route("/notificacoes/<id>", methods=["GET"])
def consultarNotificacao(id):
    notificacao = consultaNotificacao(id)
    
    if notificacao:
        Resposta["Status"] = "Sucesso"
        Resposta["Dados"] = notificacao
        Resposta["Mensagem"] = "Visualizar notificacao"
        return jsonify(Resposta)

    Resposta["Status"] = "Error"
    Resposta["Dados"] = {}
    Resposta["Mensagem"] = "Notificacao nao encontrada"
    return jsonify(Resposta)



@app.route("/alunos/<ra>/notificacoes", methods=["GET"])
def consultarNotificacaoAluno(ra):
    notificacao = consultaNotificacaoAluno(ra)
    
    if notificacao:
        Resposta["Status"] = "Sucesso"
        Resposta["Dados"] = notificacao
        Resposta["Mensagem"] = "Visualizar notificacao"
        return jsonify(Resposta)

    Resposta["Status"] = "Error"
    Resposta["Dados"] = {}
    Resposta["Mensagem"] = "Notificacao nao encontrada"
    return jsonify(Resposta)