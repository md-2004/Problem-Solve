from abc import ABC, abstractmethod

class vehical(ABC):

    @abstractmethod
    def start(self):
        pass

class car (vehical):

    def start(self):
        print("car is starting with the key.")

c = car()
c.start()

