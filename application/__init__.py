from flask import Flask
from application.model.entity.componente import Componente

app = Flask(__name__)

componente1 = Componente(1, 43, 31, 43, 54, 53, 26, 123, "12/05/2021")
componente2 = Componente(2, 12, 43, 65, 12, 65, 76, 13, "15/07/2021")
componente3 = Componente(3, 12, 53, 52, 76, 12, 43, 65, "23/08/2021")

componente_lista = [componente1, componente2, componente3]

from application.controller import home_controller