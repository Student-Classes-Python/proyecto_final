# Definición de la interfaz
import injector
from abc import ABC, abstractmethod

class IEntityService(ABC):

    @abstractmethod
    def caminar(self,hacia_donde: tuple[int,int]):
        pass

    @abstractmethod
    def montar_en_atraccion(self,atraccion:str):
        pass
