from flask import Flask,jsonify,request
import json

app = Flask(__name__)

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

@app.route("/dev/<int:id>/", methods = ["GET", "PUT", "DELETE"])
def desenvolvedor(id):
    if request.method == "GET":
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {"status": "erro", "mensagem": "Desenvolvedor de ID {} não existe".format(id)}
        return jsonify(response)
    elif request.method == "PUT":
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == "DELETE":
        desenvolvedores.pop(id)
        return jsonify({"Status": "Sucesso", "Mensagem": "Registro excluido"})
    
@app.route("/dev/", methods=['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == "POST":
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return jsonify({'status': 'Sucesso', 'Mensagem': 'Registro inserido'})
    elif request.method == "GET":
        return desenvolvedores

    

if __name__ == "__main__":
    app.run(debug=True)