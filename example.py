import injector
from abc import ABC, abstractmethod

# Definición de la interfaz
class Servicio(ABC):
    @abstractmethod
    def hacer_algo(self):
        pass

# Implementación de la interfaz
class ServicioConcreto(Servicio):
    def hacer_algo(self):
        return "Haciendo algo importante..."

class Cliente:
    @injector.inject
    def __init__(self, servicio: Servicio):
        self.servicio = servicio

    def ejecutar_servicio(self):
        return self.servicio.hacer_algo()