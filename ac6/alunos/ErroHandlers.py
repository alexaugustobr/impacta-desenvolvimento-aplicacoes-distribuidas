from Models.Resposta import Resposta
from flask import jsonify
from Server import app

@app.errorhandler(404)
def tratarErro(error):
    Resposta["Status"] = "Erro"
    Resposta["Dados"] = ""
    Resposta["Mensagem"] = "{0}".format(error)

    return jsonify(Resposta)

@app.errorhandler(500)
def tratarErro500(error):
    Resposta["Status"] = "Erro"
    Resposta["Dados"] = ""
    Resposta["Mensagem"] = "{0}".format(error)

    return jsonify(Resposta)

@app.errorhandler(403)
def tratarErro403(error):
    Resposta["Status"] = "Erro"
    Resposta["Dados"] = ""
    Resposta["Mensagem"] = "{0}".format(error)

    return jsonify(Resposta)