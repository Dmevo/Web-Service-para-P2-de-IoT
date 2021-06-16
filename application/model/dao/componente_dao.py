from application import componente_lista
from application.model.entity.componente import Componente

class ComponenteDAO:    

    def __init__(self):
        self.componente_lista = componente_lista

    def mostrar_componentes(self):
        return self.componente_lista