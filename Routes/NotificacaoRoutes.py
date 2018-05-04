from Server import app
from flask import jsonify, request
from Models.Notificacao import Notificacao
from Models.Resposta import Resposta

from Services.LerNotificacaoPorId import lerNotificacaoPorId
from Services.ListarNotificacaoPorRa import listarNotificacaoPorRa
from Services.GravarNotificacao import gravarNotificacao
from Services.FiltrarNotificacaoPorAssunto import filtrarNotificacaoPorAssunto
from Services.ExcluirNotificacao import excluiNotificacao
from Services.ArquivarNotificacao import arquivarNotificacao

@app.route("/notificacoes", methods=["POST"])
def gravarNotificacoes():
    dados = request.get_json()
    notificacao = gravarNotificacao(dados)

    if notificacao: 
        Resposta["Status"] = "Sucesso"
        Resposta["Dados"] = notificacao
        Resposta["Mensagem"] = "Notificacao gravada"
        return jsonify(Resposta)

    Resposta["Status"] = "Erro"
    Resposta["Dados"] = {}
    Resposta["Mensagem"] = "Visualizar notificaçoes"
    return jsonify(Resposta)

@app.route("/notificacoes/<id>/arquivar", methods=["GET"])
def arquivaNotificacao(id):
    Dados = request.args
    notificacao = arquivarNotificacao(id, Dados['ra'])

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
def LerNotificacaoPorIdRoute(id):
    notificacao = lerNotificacaoPorId(id)
    
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
def LerNotificacaoPorRaRoute(ra):
    notificacoes = listarNotificacaoPorRa(ra)
    
    if notificacoes:
        Resposta["Status"] = "Sucesso"
        Resposta["Dados"] = notificacoes
        Resposta["Mensagem"] = "Visualizar notificacao"
        return jsonify(Resposta)

    Resposta["Status"] = "Error"
    Resposta["Dados"] = {}
    Resposta["Mensagem"] = "Notificacao nao encontrada"
    return jsonify(Resposta)


@app.route("/alunos/<ra>/notificacoes/recebidas", methods=["GET"])
def consultarNotificacaoAlunoRecebida(ra):
    notificacao = consultaNotificacaoAlunoRecebidas(ra)
    
    if notificacao:
        Resposta["Status"] = "Sucesso"
        Resposta["Dados"] = notificacao
        Resposta["Mensagem"] = "Visualizar notificacao"
        return jsonify(Resposta)

    Resposta["Status"] = "Error"
    Resposta["Dados"] = {}
    Resposta["Mensagem"] = "Notificacao nao encontrada"
    return jsonify(Resposta)

@app.route("/alunos/<ra>/notificacoes/atividades", methods=["GET"])
def consultarNotificacaoDeAtividade(ra):
    notificacao = filtrarNotificacaoPorAssunto("Atividades", ra)
    if len(notificacao) != 0:
        Resposta["Status"] = "Sucesso"
        Resposta["Dados"] = notificacao
        Resposta["Mensagem"] = "Visualizar notificacao"
        return jsonify(Resposta)
    Resposta["Status"] = "Error"
    Resposta["Dados"] = {}
    Resposta["Mensagem"] = "Notificacao nao encontrada"
    return jsonify(Resposta)

@app.route("/alunos/<ra>/notificacoes/trabalhos", methods=["GET"])
def consultarNotificacaoDeTrabalho(ra):
    notificacao = filtrarNotificacaoPorAssunto("Trabalhos", ra)
    if len(notificacao) != 0:
        Resposta["Status"] = "Sucesso"
        Resposta["Dados"] = notificacao
        Resposta["Mensagem"] = "Visualizar notificacao"
        return jsonify(Resposta)
    Resposta["Status"] = "Error"
    Resposta["Dados"] = {}
    Resposta["Mensagem"] = "Notificacao nao encontrada"
    return jsonify(Resposta)

@app.route("/alunos/<ra>/notificacoes/comunicacoesdiversas", methods=["GET"])
def consultarNotificacaoDeComunicacoes(ra):
    notificacao = filtrarNotificacaoPorAssunto("Comunicações diversas", ra)
    if len(notificacao) != 0:
        Resposta["Status"] = "Sucesso"
        Resposta["Dados"] = notificacao
        Resposta["Mensagem"] = "Visualizar notificacao"
        return jsonify(Resposta)
    Resposta["Status"] = "Error"
    Resposta["Dados"] = {}
    Resposta["Mensagem"] = "Notificacao nao encontrada"
    return jsonify(Resposta)

@app.route("/notificacoes/<id>", methods=["DELETE"])
def deletarNotificacao(id):
    notificacao = excluiNotificacao(id)
    
    if notificacao:
        Resposta["Status"] = "Sucesso"
        Resposta["Dados"] = notificacao
        Resposta["Mensagem"] = "Visualizar notificacao"
        return jsonify(Resposta)

    Resposta["Status"] = "Error"
    Resposta["Dados"] = {}
    Resposta["Mensagem"] = "Notificacao nao encontrada"
    return jsonify(Resposta)