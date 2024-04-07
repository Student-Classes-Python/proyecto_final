from services.ieconomyservice import IEconomyService

class EconomyService(IEconomyService):
    def __init__(self, saldo: int) -> None:
        self.saldo = saldo

    def recibir_dinero(self, dinero: int) -> None:
        self.saldo += dinero
        pass

    def obtener_saldo(self) -> int:
        return self.saldo