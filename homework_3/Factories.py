from abc import ABC, abstractmethod

class BaseFactory(ABC):
    @abstractmethod
    def makeOrder(self, id: int) -> list:
        pass
    
class HamburgerFactory(BaseFactory):
    def makeOrder(self, id):        
        return ["Hamburger", id]
    
class PizzaFactory(BaseFactory):
    def makeOrder(self, id):        
        return ["Pizza", id]