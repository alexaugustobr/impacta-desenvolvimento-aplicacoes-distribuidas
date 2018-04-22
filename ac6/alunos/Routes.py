from Server import app
from flask import jsonify
from flask import request
from Services.AtualizarAluno import atualizarAluno
from Services.CadastrarAluno import cadastrarAluno
from Services.ListarAluno import listarAlunos
from Services.ConsultarAluno import consultarAluno
from Models.Aluno import Aluno
from Models.Resposta import Resposta

@app.route("/alunos", methods=["GET"])
def listarAluno():
    alunos = listarAlunos()
    if len(alunos) == 0: 
        Resposta["Status"] = "Sucesso"
        Resposta["Dados"] = []
        Resposta["Mensagem"] = "Não há alunos"

        return jsonify(Resposta)

    Resposta["Status"] = "Sucesso"
    Resposta["Dados"] = alunos
    Resposta["Mensagem"] = "Lista Alunos"

    return jsonify(Resposta)

@app.route("/alunos/<ra>", methods=["GET"])
def consultaAluno(ra):
    aluno = consultarAluno(ra)

    if aluno:
        Resposta["Status"] = "Sucesso"
        Resposta["Dados"] = aluno
        Resposta["Mensagem"] = "Consulta de Alunos"
        return jsonify(Resposta)

    Resposta["Status"] = "Error"
    Resposta["Dados"] = {}
    Resposta["Mensagem"] = "Aluno não encontrado"
    return jsonify(Resposta)

@app.route("/alunos", methods=["POST"])
def cadastroAluno():
    dados = request.get_json()

    aluno = cadastrarAluno({"ra":dados["ra"], "nome":dados["nome"]})

    Resposta["Status"] = "Sucesso"
    Resposta["Dados"] = aluno
    Resposta["Mensagem"] = "Aluno Cadastrado"

    return jsonify(Resposta)

@app.route("/alunos", methods=["PUT"])
def atualizaAluno():
    dados = request.get_json()

    aluno = atualizarAluno({"ra":dados["ra"], "nome":dados["nome"]})

    if aluno:
        Resposta["Status"] = "Sucesso"
        Resposta["Dados"] = aluno
        Resposta["Mensagem"] = "Consulta de Alunos"
        return jsonify(Resposta)

    Resposta["Status"] = "Error"
    Resposta["Dados"] = {}
    Resposta["Mensagem"] = "Aluno não encontrado"
    return jsonify(Resposta)