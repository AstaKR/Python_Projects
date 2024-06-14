from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
my_moneymachine = MoneyMachine()
my_coffee_maker = CoffeeMaker()
menu = Menu()
my_moneymachine.report()
my_coffee_maker.report()

is_machine_on = True

while is_machine_on:
    option = menu.get_items()
    choice = input(f"Enter the drink name {option}").lower()
    if choice == "off":
        is_machine_on = False
    elif choice == "report":
        my_coffee_maker.report()
        my_moneymachine.report()
    else:
        drinks = menu.find_drink(choice)
        if my_coffee_maker.is_resource_sufficient(drinks) and my_moneymachine.make_payment(drinks.cost):
            my_coffee_maker.make_coffee(drinks)