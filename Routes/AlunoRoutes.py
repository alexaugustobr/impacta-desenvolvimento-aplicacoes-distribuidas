from Server import app
from flask import jsonify, request
from Models.Resposta import Resposta

from Services.AtualizarAluno import atualizarAluno
from Services.CadastrarAluno import cadastrarAluno
from Services.DeletarAluno import deletarAluno
from Services.ListarAluno import listarAlunos
from Services.ConsultaAluno import consultaAluno

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
def consultarAluno(ra):
    aluno = consultaAluno(ra)

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