import os

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 300,
}


def has_supplies(drink):
    """Confirm (bool) enough resources to make drink (str)."""
    supplies_ok = True
    for item, qty in MENU[drink]["ingredients"].items():
        if qty > resources[item]:
            supplies_ok = False

    return supplies_ok


def make_drink(drink):
    """Digitally consume resources."""
    for item, qty in MENU[drink]["ingredients"].items():
        resources[item] -= qty


def clear_termnial():
    """Clear terminal screen of Windows and UNIX-like system."""
    os.system("cls" if os.name == "nt" else "clear")


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


def get_payment(drink):
    """Take in patron currency and return total (float)."""
    valid_money = {"quarters": 0.25, "dimes": 0.1, "nickles": 0.05, "pennies": 0.01}

    payment = []
    for money in valid_money:
        deposit = prompt_user(
            f"How many {money}?:\t", [str(number) for number in range(0, 101)]
        )
        payment.append(float(deposit) * valid_money[money])

    return sum(payment)


def get_change(drink, payment):
    """Return difference (float) of payment (float) and drink (str) cost (float)."""
    return payment - MENU[drink]["cost"]


powered_on = True
while powered_on:
    clear_termnial()

    menu_items = list(MENU.keys())
    beverage = prompt_user(
        f"\n{menu_items}" + "\nWhich would you like?: ",
        [items for items in menu_items] + ["report"],
    )

    if beverage == "report":
        for res, qty in resources.items():
            print(f"{res}\t{qty}")
    elif has_supplies(beverage):
        patron_payment = get_payment(beverage)
        drink_cost = MENU[beverage]["cost"]

        if patron_payment >= drink_cost:
            make_drink(beverage)

            if patron_payment > drink_cost:
                print(f"Here is {get_change(beverage, patron_payment)} in change.")
            print(f"!!!HERE IS YOUR {beverage.upper()}. ENJOY!!!")
        elif patron_payment < drink_cost:
            print("!!!INSUFFICIENT FUNDS!!!")
    else:
        print("!!!LOW ON SUPPLIES!!!")

    more_orders = prompt_user(
        "\nWould you like to place another order? (y|n): ", ["y", "n"]
    )
    if more_orders == "n":
        powered_on = not powered_on
