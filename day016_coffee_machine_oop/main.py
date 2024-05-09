from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

coffee_drinks = menu.get_items().split('/')
drink_ordered = None


def select_drink():
    print("Type a drink listed below to begin:")
    for drink_option in coffee_drinks:
        print(drink_option)

    global drink_ordered
    drink_ordered = input("> ").strip().lower()


def manager_report():
    coffee_maker.report()
    money_machine.report()


def newline():
    print("")


machine_on = True
while machine_on:
    newline()
    select_drink()
    if drink_ordered == "off":
        machine_on = False
    elif drink_ordered == "report":
        newline()
        manager_report()
    elif menu.find_drink(drink_ordered) is not None:
        drink_ordered = menu.find_drink(drink_ordered)
        newline()
        can_make_drink = coffee_maker.is_resource_sufficient(drink_ordered)
        if can_make_drink is True:
            if money_machine.make_payment(drink_ordered.cost) is True:
                newline()
                coffee_maker.make_coffee(drink_ordered)
