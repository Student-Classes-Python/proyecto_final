from abc import ABC, abstractmethod
from models.data_model import DataModel
from services.bases.ipricingStrategyService import IPricingStrategyService

class IMLPricingStrategyService(IPricingStrategyService):
    @abstractmethod
    def obtener_datos(self, data_model: DataModel) -> None:
        pass
    # @abstractmethod
    # def obtener_saldo(self) -> int:
    #     pass