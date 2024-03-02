from os import system, name

def bill_split():
    # clear terminal (unix or windows)
    system("cls" if name == "nt" else "clear")
    
    # prompt user welome & enter bill total
    bill_total = input("Welcome User\n \nPlease enter bill total: \n")
    
    # get gradituity
    stnd_tips = [10, 12, 15, 20, 22, 25, 30, 32, 25, 40]
    print("\nWhat tip percentage will be give: ")
    for tip in stnd_tips:
        print(tip)
    tip_pct = input("\nEnter percentage here: ")
    if tip_pct in stnd_tips:
        head_count = input("\n\nHow many people are splitting the bill:\n")
    else:
        head_count = input(f"\n{tip_pct} % is very generous. \n\nHow many people are splitting the bill: ")
    
    # calculate splits, prompt user    
    split = round((float(bill_total) * (1 + float(tip_pct) / 100)) / int(head_count), 2)
    system("cls" if name == "nt" else "clear")
    print(f"\nEvery person should pay: ${split}")
    
if __name__ == '__main__':
    bill_split()