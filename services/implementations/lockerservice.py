import injector
from services.ilockerservice import ILockersService
from services.ieconomyservice import IEconomyService


class LockersService(ILockersService):
   
  @injector.inject    
  def __innit__(self) -> None:
    # self.get_number_for_locker = get_number_for_locker
    # self.get_locker_price = get_locker_price
    # self.get_occupied_lockers = get_occupied_lockers
    self.counter = 0
    self.total = 0
    self.cost = 10
    # self.economyService = economyService

  def get_number_for_locker(self) -> int:
    #locker_number= self.get_number_for_locker
    self.counter += 1 
    print(f"tu numero de taquilla es {self.counter}")
    return self.counter
  
  def sell_entrance_ticket(self, economyService : IEconomyService ) -> None:
      #cost= self.sell_entrance_ticket
      self.total =self.cost * self.counter
      economyService.recibir_dinero(self.cost)
      print(f"venta realizada,total a pagar {self.total}$")
      
  def change_cost(self, cost : int) -> None:
      self.cost=cost