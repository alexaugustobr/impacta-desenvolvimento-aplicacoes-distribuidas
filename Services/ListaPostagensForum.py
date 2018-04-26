from Server import foruns
from flask import jsonify


def listaPostagensForum():
    return foruns

@app.route("/forum", methods=["GET"])
def listaPostagensForuns():
    foruns = listaPostagensForum()
    Resposta = {"Status":"","Dados":"", "Mensagem":""}

    if len(foruns) == 0: 
        Resposta["Status"] = "Sucesso"
        Resposta["Dados"] = []
        Resposta["Mensagem"] = "Nao ha foruns"

        return jsonify(Resposta)

    Resposta["Status"] = "Sucesso"
    Resposta["Dados"] = foruns
    Resposta["Mensagem"] = "Lista postagens"

    return jsonify(Resposta)