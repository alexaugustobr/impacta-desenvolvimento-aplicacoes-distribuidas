from Server import app
from flask import jsonify, request
from Models.Resposta import Resposta

from Services.AtualizarProfessor import atualizarProfessor
from Services.CadastrarProfessor import cadastrarProfessor
from Services.ListarProfessor import listarProfessors
from Services.ConsultaProfessor import consultaProfessor

@app.route("/professores", methods=["GET"])
def listarProfessor():
    professores = listarProfessors()
    if len(professores) == 0: 
        Resposta["Status"] = "Sucesso"
        Resposta["Dados"] = []
        Resposta["Mensagem"] = "Nao ha professores"

        return jsonify(Resposta)

    Resposta["Status"] = "Sucesso"
    Resposta["Dados"] = professores
    Resposta["Mensagem"] = "Lista Professors"

    return jsonify(Resposta)

@app.route("/professores/<ra>", methods=["GET"])
def consultarProfessor(ra):
    professor = consultaProfessor(ra)

    if professor:
        Resposta["Status"] = "Sucesso"
        Resposta["Dados"] = professor
        Resposta["Mensagem"] = "Consulta de Professors"
        return jsonify(Resposta)

    Resposta["Status"] = "Error"
    Resposta["Dados"] = {}
    Resposta["Mensagem"] = "Professor nao encontrado"
    return jsonify(Resposta)

@app.route("/professores", methods=["POST"])
def cadastroProfessor():
    dados = request.get_json()

    professor = cadastrarProfessor({"ra":dados["ra"], "nome":dados["nome"]})

    Resposta["Status"] = "Sucesso"
    Resposta["Dados"] = professor
    Resposta["Mensagem"] = "Professor Cadastrado"

    return jsonify(Resposta)

@app.route("/professores/<ra>", methods=["PUT"])
def atualizaProfessor(ra):
    dados = request.get_json()

    professor = atualizarProfessor({"ra":dados["ra"], "nome":dados["nome"]},ra)

    if professor:
        Resposta["Status"] = "Sucesso"
        Resposta["Dados"] = professor
        Resposta["Mensagem"] = "Professor atualizado"
        return jsonify(Resposta)

    Resposta["Status"] = "Error"
    Resposta["Dados"] = {}
    Resposta["Mensagem"] = "Professor nao encontrado"
    return jsonify(Resposta)