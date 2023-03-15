from abc import abstractmethod

class Vehiculo_deportivos ():
    @abstractmethod
    def velocidad_maxima(self):
        pass

class Nissan(Vehiculo_deportivos):
    def velocidad_maxima(self, modelo, velocidad):
        super().velocidad_maxima()
        self.modelo = modelo
        self.velocidad = velocidad
        return ('El deportivo {} que alcanza la velocidad de {} '.format(self.modelo, self.velocidad))
    
class Toyota(Vehiculo_deportivos):
    def velocidad_maxima(self, modelo, velocidad):
        super().velocidad_maxima()
        self.modelo = modelo
        self.velocidad = velocidad
        return ('El deportivo {} que alcanza la velocidad de {} '.format(self.modelo, self.velocidad))
    
class Mazda(Vehiculo_deportivos):
    def velocidad_maxima(self, modelo, velocidad):
        super().velocidad_maxima()
        self.modelo = modelo
        self.velocidad = velocidad   
        return ('El deportivo {} que alcanza la velocidad de {} '.format(self.modelo, self.velocidad))
    
depo1 = Nissan()
depo2 = Toyota()
depo3 = Mazda()

print(depo1.velocidad_maxima("Nissan GRT R35", "315 km/h"))
print(depo2.velocidad_maxima("Toyota Supra MK4", "387 km/h"))
print(depo3.velocidad_maxima("Mazda RX7", "250 km/h"))

#Asi le entendi:/