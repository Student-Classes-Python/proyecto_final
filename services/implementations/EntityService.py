import injector
from services.IEntityService import IEntityService

class EntityService(IEntityService):

    def __init__(self,nombre,edad):
        super.__init__()
        self.nombre = nombre
        self.edad = edad

    def caminar(self,hacia_donde: tuple[int,int]) -> None:
        self.posicion = [hacia_donde[0],hacia_donde[1]]
        pass


    def montar_en_atraccion(self,atraccion:str):
        # TO DO
        return f'{self.nombre} se ha divertido.'

    
    def pagar_la_entrada(self,numero_personas):
        # TO DO: Pagar el precio del taquillero
        # nombre_del_economyservice.recibir_dinero(acceder al precio con PricingStrategyService)
        pass
