from abc import ABC, abstractmethod
from models.data_model import DataModel
from services.imlPricingStrategyService import IMLPricingStrategyService

class MLPricingStrategyService(IMLPricingStrategyService):
    def obtener_datos(self, data_model: DataModel) -> None:
        
        pass
    # @abstractmethod
    # def obtener_saldo(self) -> int:
    #     pass