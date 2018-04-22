import requests as req

url = "http://localhost:5000/alunos"
aluno = {"ra":"1", "nome":"aluno1"}


retorno = req.api.post(url,json=aluno).json()
print("Cadastro")
print(retorno)


retorno = req.api.get(url).json()
print("Lista")
print(retorno)

aluno = {"ra":"1", "nome":"novo nome"}

retorno = req.api.put(url+"/1",json=aluno).json()
print("Atualizacao")
print(retorno)


retorno = req.api.get(url).json()
print("Lista")
print(retorno)

retorno = req.api.delete(url+"/1").json()
print("Deletar")
print(retorno)

retorno = req.api.get(url).json()
print("Lista")
print(retorno)