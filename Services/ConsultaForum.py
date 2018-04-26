from Server import foruns
from flask import jsonify

def consultarForum(ForumId):
    for forum in foruns:
        if str(forum["ForumId"]) == str(ForumId):
            return forum
    return None

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