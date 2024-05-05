from abc import ABC, abstractmethod

class ILockersService(ABC):
    @abstractmethod
    def get_number_for_locker(self) -> int:
        pass

    @abstractmethod
    def sell_entrance_ticket(self) -> None:
        pass
        
    @abstractmethod
    def change_cost(self, cost : int) -> None:
        pass

    # @abstractmethod
    # def get_occupied_lockers(self):
    #     pass



