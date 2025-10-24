from art import logo


def calculator():
    """Execute calculations.
    
    Prompts:
        - n1 (float): Number or decimal.
        - n2 (float): Number or decimal.
        - op (str): Math operation.
        - next op (str): Continue or start new calculation, or exit
    
    Returns:
        None: Print result to terminal.
        
    Raises:
        ValueError: Invalid prompt input."""
    print(logo)

    try:
        use_result = False
        operating = True
        while operating:
            if not use_result:
                n1 = input("Enter value:\t").strip()
                n2 = input("Enter value:\t").strip()
            else:
                n2 = input("Enter value:\t").strip()
            try:
                n1 = float(n1)
                n2 = float(n2)
            except ValueError():
                print("One or both inputs not float type.")

            ops = ["+", "-", "/", "*", "^"]
            op = input(f"Enter {ops}:\t").strip()
            op_str = f"{n1} {op.replace('^', '**')} {n2}"
            if op in ops:
                result = eval(op_str)
                print(f"{op_str}: {result}")
            else:
                raise ValueError(
                    f"Invalid operation input {op}. Operations include {ops}."
                )

            next_op = (
                input("\ny - continue" + "\nn - new calculation" + "\nx - exit\n: ")
                .strip()
                .lower()
            )
            if next_op == "y":
                n1 = result
                use_result = True
            elif next_op == "n":
                use_result = False
            elif next_op == "x":
                break
            else:
                raise ValueError("Invalid input. Expecting y, n, or x.")

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    calculator()
