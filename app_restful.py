from flask import Flask, request
from flask_restful import Resource, Api
import json


app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        "id": 0,
        "Nome": "Ruan Victor",
        "Tecnologias": ["Python", "Django"]
     },
     {
         "id": 1,
        "Nome": "Artur Bruno",
        "Tecnologias": ["React", "Js", "java"]
     }
]


class Developer(Resource):
    id = len(desenvolvedores)
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {"status": "erro", "mensagem": "Desenvolvedor de ID {} nao existe".format(id)}
        return (response)
    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return (dados)
    def delete(self, id):
        desenvolvedores.pop(id)
        return ({"Status": "Sucesso", "Mensagem": "Registro excluido"})

class List_Developer(Resource):
    def post(self):
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return ({f'status': 'Sucesso', 'Mensagem': 'Registro inserido'})
    def get(self):
        return desenvolvedores

api.add_resource(Developer, "/dev/<int:id>/")
api.add_resource(List_Developer, "/dev/")



if __name__ == "__main__":
    app.run(debug=True)
