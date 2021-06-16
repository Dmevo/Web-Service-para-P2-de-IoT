from flask import Flask
from application.model.entity.componente import Componente
from datetime import datetime

app = Flask(__name__)

componente1 = Componente(43, 31, 43, 54, 53, 26, 123, datetime.now())
componente2 = Componente(12, 43, 65, 12, 65, 76, 13, datetime.now())
componente3 = Componente(12, 53, 52, 76, 12, 43, 65, datetime.now())

componente_lista = [componente1, componente2, componente3]

from application.controller import home_controller