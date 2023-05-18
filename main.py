from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


is_on = True
while is_on:
    options = menu.get_items()
    escolha = input(f"Qual você gostaria? ({options}): ")
    if escolha == "off":
        is_on = False
    elif escolha == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(escolha)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)








