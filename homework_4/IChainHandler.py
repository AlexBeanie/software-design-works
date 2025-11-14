from abc import ABC, abstractmethod

class IChainHandler(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass
    
    @abstractmethod
    def handle(self):
        pass