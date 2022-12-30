from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    choice = menu.get_items()
    what_you_want = input(f"What drink do you want? You can choose /{choice}")

#TODO - Print report
    if what_you_want == "report":
        coffee_maker.report()
        money_machine.report()
    elif what_you_want == "off":
        is_on = False
    else:
        drink = menu.find_drink(what_you_want)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
#TODO - Check resource sufficient

#TODO - Process coins

#TODO - Check transaction successful?

#TODO - Make coffee

