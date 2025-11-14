from IChainHandler import IChainHandler
from order import Order
from abc import abstractmethod

class BaseChainHandler(IChainHandler):
    def __init__(self):
        self.handler = None
             
    def set_next(self, handler: IChainHandler):
        self.next = handler
        return handler
    
    def handle(self, order: Order):
        self._try(order)
        if self.next.handler is not None:
            self.next.handle(order)            
        
    @abstractmethod
    def _try():
        pass