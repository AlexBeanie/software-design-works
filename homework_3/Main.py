from Factories import HamburgerFactory, PizzaFactory
from Services import Services

NUM_THREADS = 3

if __name__ == "__main__":
    services = Services()
    hamburgerFactory = HamburgerFactory()
    pizzaFactory = PizzaFactory()
    
    for i in range(5):        
        pedido = hamburgerFactory.makeOrder(i) if i % 2 == 0 else pizzaFactory.makeOrder(i)
        services.addOrder(pedido)
    
    services.processOrders(NUM_THREADS)
