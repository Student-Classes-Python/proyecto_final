from abc import ABC, abstractmethod

class IEconomyService(ABC):
    @abstractmethod
    def recibir_dinero(self, dinero: int) -> None:
        pass
    @abstractmethod
    def obtener_saldo(self) -> int:
        pass
