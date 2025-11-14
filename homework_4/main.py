from order import Order
from meal import Meal, MealType
from chainHandlers import PrepHandler, NotifHandler

def startProcess(orders, handler):
    for order in orders:
        handler.handle(order)

if __name__ == "__main__":
    preparator = PrepHandler()
    notificator = NotifHandler()
    preparator.set_next(notificator)
    
    burger = Meal("Hamburguesa", MealType.FOOD)
    burger.add_ingredient("Carne")
    burger.add_ingredient("Queso")
    burger.add_ingredient("Tomate")

    soda = Meal("Refresco", MealType.DRINK)
    soda.add_ingredient("Hielo")
    soda.add_ingredient("Azúcar")

    pizza = Meal("Pizza", MealType.FOOD)
    pizza.add_ingredient("Queso")
    pizza.add_ingredient("Pepperoni")
    
    water = Meal("Agua", MealType.DRINK)
    water.add_ingredient("Hielo")

    coffee = Meal("Café", MealType.DRINK)
    coffee.add_ingredient("Leche")
    coffee.add_ingredient("Azúcar")

    # Crear una orden y agregar meals
    order1 = Order(101)
    order1.meals.append(burger)
    order1.meals.append(soda)
    order1.meals.append(pizza)
    
    order2 = Order(202)
    order2.meals.append(water)
    order2.meals.append(coffee)
    
    startProcess([order1, order2], preparator)
    
    