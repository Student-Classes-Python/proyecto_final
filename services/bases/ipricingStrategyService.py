from abc import ABC, abstractmethod
from models.data_model import DataModel

class IPricingStrategyService(ABC):
    @abstractmethod
    def obtener_datos(self, data_model: DataModel) -> None:
        pass
    # @abstractmethod
    # def obtener_saldo(self) -> int:
    #     pass