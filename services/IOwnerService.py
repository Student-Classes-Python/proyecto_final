import injector
from abc import ABC, abstractmethod
from IEntityService import IEntityService

# Implementación de la interfaz del dueño
class IOwnerService(IEntityService):

    #Entrar y verificar que es el dueño
    @abstractmethod
    def entrar_como_dueño(self,contraseña_ingresada):
        super.__init__()
        pass
    
    
    @abstractmethod
    def montar_en_atraccion(self,atraccion:str):
        pass

    #Acceder a informacion del parque como las personas que han entrado o el dinero recaudado
    @abstractmethod
    def revisar_informacion(self,que_informacion: str):
        pass

    #Irse del parque (como cerrar sesion)
    @abstractmethod
    def irse_del_parque(self,contraseña:str):
        pass

    @abstractmethod
    def caminar(self,hacia_donde:str):
        pass

    @abstractmethod
    def cambiar_precio(self,precio):
        pass