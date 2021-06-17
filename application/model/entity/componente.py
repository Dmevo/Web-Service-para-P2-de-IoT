
class Componente:

    def __init__(self, detector_id, ozonio, particula, monoxido_carbono, oxido_nitroso, gas_inflamavel, temperatura, umidade, data):
        self.detector_id = detector_id
        self.ozonio = ozonio
        self.particula = particula
        self.monoxido_carbono = monoxido_carbono
        self.oxido_nitroso = oxido_nitroso
        self.gas_inflamavel = gas_inflamavel
        self.temperatura = temperatura
        self.umidade = umidade
        self.data = data

    def set_id(self, id):
        self.detector_id = id

    def get_id(self):
        return self.detector_id

    def set_ozonio(self, ozonio):
        self.ozonio = ozonio

    def get_ozonio(self):
        return self.ozonio

    def set_particula(self, particula):
        self.particula = particula

    def get_particula(self):
        return self.particula

    def set_carbono(self, carbono):
        self.monoxido_carbono = carbono

    def get_carbono(self):
        return self.monoxido_carbono

    def set_nitroso(self, nitroso):
        self.oxido_nitroso = nitroso
    
    def get_nitroso(self):
        return self.oxido_nitroso

    def set_gas(self, gas_inflamavel):
        self.gas_inflamavel = gas_inflamavel

    def get_gas(self):
        return self.gas

    def set_temperatura(self, temperatura):
        self.temperatura = temperatura
    
    def get_temperatura(self):
        return self.temperatura

    def set_umidade(self, umidade):
        self.umidade = umidade

    def get_umidade(self):
        return self.umidade

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def toDict(self):
        return {
            "detector id":self.detector_id,
            "data":self.data,
            "ozonio":self.ozonio,
            "particula":self.particula,
            "monoxido de carbono":self.monoxido_carbono,
            "oxido nitroso":self.oxido_nitroso,
            "gas inflamavel":self.gas_inflamavel,
            "temperatura":self.temperatura,
            "umidade":self.umidade
        }