from flask import jsonify, request
from application import app
from application.model.dao.componente_dao import ComponenteDAO
from application.model.entity.componente import Componente

componente_dao = ComponenteDAO()
componente_lista = componente_dao.mostrar_componentes()

@app.route("/componentes", methods=['GET'])
def listar_componentes():
    componentes_dict_lista = []
    for componente in componente_lista:
        componentes_dict_lista.append(componente.toDict())
    return (jsonify(componentes_dict_lista))

@app.route("/componentes", methods=['POST'])
def add_componentes():
    detector_id = request.json["detector id"]
    data = request.json["data"]
    ozonio = request.json["ozonio"]
    particula = request.json["particula"]
    carbono = request.json["monoxido de carbono"]
    oxido = request.json["oxido nitroso"]
    gas = request.json["gas inflamavel"]
    temperatura = request.json["temperatura"]
    umidade = request.json["umidade"]
    componentes = Componente(detector_id, ozonio, particula, carbono, oxido, gas, temperatura, umidade, data)
    componente_lista.append(componentes)
    return componentes.toDict(), 201

@app.route("/componentes/<id>", methods=['GET'])
def busca_detector(id):
    for componentes in componente_lista:
        if componentes.get_id() == int(id):
            return componentes.toDict()
    return jsonify(""), 404