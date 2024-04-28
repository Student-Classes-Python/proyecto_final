from abc import ABC, abstractmethod

class ILockersService(ABC):
    @abstractmethod
    def get_number_for_locker(self):
        pass

    @abstractmethod
    def get_locker_price(self):
        pass

    # @abstractmethod
    # def get_occupied_lockers(self):
    #     pass



class LockersService(ILockersService):
   
    def __innit__(self):
      #  self.get_number_for_locker = get_number_for_locker
      # self.get_locker_price = get_locker_price
      # self.get_occupied_lockers = get_occupied_lockers
      self.counter = 0
      self.total = 0
      self.cost = 10

    def get_number_for_locker(self):
      #locker_number= self.get_number_for_locker
      self.counter += 1 
      print(f"tu numero de taquilla es {self.counter}")
      return self.counter
    
    def sell_entrance_ticket(self):
        #cost= self.sell_entrance_ticket
        self.total =self.cost * self.counter
        return print(f"venta realizada,total a pagar {self.total}$")
        
    def change_cost(self, cost : int):
        self.cost=cost