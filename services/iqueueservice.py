
from abc import ABC, abstractmethod

class IQueueService(ABC):
    """Servicio para la gestión de colas en las atracciones."""

    def __init__(self):
        self.visitants = []
        self.n_can = 0 
    
    @abstractmethod
    def vacio(self):
        pass
        
    @abstractmethod
    def enqueue(self, visitor_id: int) -> None:
        """Agrega un visitante a la cola."""
        pass

    @abstractmethod
    def dequeue(self) -> int:
        """Retira el primer visitante de la cola."""
        pass

    @abstractmethod
    def size(self) -> int:
        """Devuelve el número total de visitantes en la cola."""
        pass

