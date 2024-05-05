from abc import abstractmethod, ABC

class ITimeService(ABC):

    @abstractmethod
    def advance_time(self):
        pass

    @abstractmethod
    def adjust_time_velocity(self):
        pass

    @abstractmethod
    def get_time(self):
        pass