from flask import render_template, jsonify
from application import app
from application.model.dao.componente_dao import ComponenteDAO
from application.model.entity.componente import Componente

componente_dao = ComponenteDAO()
componente_lista = componente_dao.mostrar_componentes()

@app.route("/", methods=['GET'])
def home():
    componentes_dict_lista = []
    for componente in componente_lista:
        componentes_dict_lista.append(componente.toDict())
    return (jsonify(componentes_dict_lista))

