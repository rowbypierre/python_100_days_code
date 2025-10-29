from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
menu_items  = [item for item in menu.get_items().split("/")
               if len(item) > 0]

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

def prompt_user(prompt, valid_input_list):
    """Prompt user input and return valid input."""
    prompting = True
    while prompting:
        try:
            user_input = input(prompt).strip().lower()
            if user_input not in valid_input_list:
                raise ValueError(
                    f"'{user_input}' Invalid. Expected: {valid_input_list}"
                )
            else:
                prompting = not prompting
                return user_input
        except Exception as error:
            print(f"Error: {error}")


servicing = True
while servicing:
    coffee_choice = prompt_user(
        f"\n{menu_items}" + "\nWhich would you like?: ",
        [items for items in menu_items] + ["report"],
    )

    if coffee_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        coffee_choice = menu.find_drink(coffee_choice)
        
        if coffee_maker.is_resource_sufficient(coffee_choice):
            full_payment = money_machine.make_payment(coffee_choice.cost)
            if full_payment:
                coffee_maker.make_coffee(coffee_choice)

    more_orders = prompt_user(
        "\nWould you like to place another order? (y|n): ", ["y", "n"]
    )
    no_more_orders = more_orders == "n"
    if no_more_orders:
        servicing = not servicing