import injector
from example import Servicio, ServicioConcreto, Cliente

# Módulo de inyección que configura las dependencias
class ModuloDeAplicacion(injector.Module):
    def configure(self, binder):
        binder.bind(Servicio, to=ServicioConcreto)