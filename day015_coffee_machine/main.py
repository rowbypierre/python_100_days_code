import locale
import sys

# TODO: Create menu with 3 hot flavors, and ingredients.
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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 300,
}


# TODO: Prompt menu (brew drink) or report (summary of consumables).
functions = {
    "1": {
        "component": MENU,
        "alias": "Menu"
    },
    "2": {
        "component": resources,
        "alias": "Report"
    },
    "3": {
        "component": "sys.exit()",
        "alias": "Exit"
    }
}

profit = 0
coffee_machine_running = True

while coffee_machine_running:
    counter = 0
    for operation in functions:
        counter += 1
        print(f"Enter {counter} |\t\t{functions[operation]["alias"]}")

    function_selection = input("> ")
    if function_selection == "1":
        # TODO: Prompt coffee options, user input selecting one drink.
        print("\nSelect drink below:")
        counter = 0
        for item in MENU:
            counter += 1
            MENU[item]["line_number"] = counter
            print(f"Enter '{MENU[item]["line_number"]}' |\t\t{item.capitalize()}")

        user_selection = int(input("> ").strip())
        for item in MENU:
            if MENU[item]["line_number"] == user_selection:
                user_selection = item

        # TODO: Confirm enough resources exist to brew drink.
        return_to_menu = False
        for resource in MENU[user_selection]["ingredients"]:
            if resources[resource] < MENU[user_selection]["ingredients"][resource]:
                print("\nMachine is low on ingredients needed to make this drink.")
                return_to_menu = True
                break

        if return_to_menu is not True:
            for ingredient in resources:
                if ingredient not in list(MENU[user_selection]["ingredients"].keys()):
                    MENU[user_selection]["ingredients"][ingredient] = 0
                resources[ingredient] -= MENU[user_selection]["ingredients"][ingredient]
                # print(str(ingredient) + ":\t" + str(resources[ingredient]))

            # TODO: Confirm drink selection, print drink price. Finally prompt/input user digital currency.
            locale.setlocale(locale.LC_ALL, '')

            def convert_int_to_usd(amount):
                """
                Returns parameter 'amount' (numeric value) as U.S. dollar currency.
                """
                local_value = locale.currency(amount, symbol=True, grouping=True)
                return local_value

            print(f"\n{user_selection.capitalize()} cost {convert_int_to_usd(MENU[user_selection]["cost"])}.")

            accepted_coins = {
                "Penny": {
                    "conversion_rate": .01
                },
                "Nickel": {
                    "conversion_rate": .05
                },
                "Dime": {
                    "conversion_rate": .10
                },
                "Quarter": {
                    "conversion_rate": .25
                }
            }

            print("\nEnter coins:")
            deposit = 0
            continue_depositing = True
            while continue_depositing:
                for coin in accepted_coins:
                    coin_deposit_count = int(input(f"{coin}(s) deposited: ").strip())
                    deposit += coin_deposit_count * accepted_coins[coin]["conversion_rate"]
                    print("Deposit total: " + convert_int_to_usd(deposit))

                    if deposit >= MENU[user_selection]["cost"]:
                        print(f"\nNo additional deposits required.")
                        continue_depositing = False

                        # TODO: Calculate customer change, profits, and resources after transaction.
                        if deposit > MENU[user_selection]["cost"]:
                            customer_change = deposit - MENU[user_selection]["cost"]
                            profit = deposit - customer_change
                            print("Change returned to customer:\t" + convert_int_to_usd(customer_change))
                        else:
                            profit += MENU[user_selection]["cost"]

                        print("\nBrewing...")
                        # print("profit:\t" + str(convert_int_to_usd(profit)))
                        break
                    elif deposit < MENU[user_selection]["cost"]:
                        print(f"Deposit {convert_int_to_usd(MENU[user_selection]["cost"] - deposit)} for drink.\n")
    # TODO: Print ingredient inventory.
    elif function_selection == "2":
        print("")

        for ingredient in resources:
            print(ingredient.capitalize() + ":\t" + str(resources[ingredient]))
    # TODO: Provide option to exit program.
    elif function_selection == "3":
        exec(functions[function_selection]["component"])

    if int(input("\nPerform another operation? \nEnter 1 |\t'Yes' \nEnter 2 |\t'No'\n> ").strip()) != 1:
        exec(functions["3"]["component"])
    else:
        print("")
