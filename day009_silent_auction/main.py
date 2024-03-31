import os,time
from art import auction_sign

def clear():
    time.sleep(1)
    os.system("cls" if os.name == "nt" else "clear")
    
def silent_auction():
    more_bidders = 1
    bids = []
    id = 0
    while more_bidders == 1:
        clear()
        print(auction_sign)
        id += 1
        bid_entry = {}
        
        name = input("\nEnter name: \n> ").strip().split(" ")
        for position in name:
            if name[0] == position:
                position = position.lower().capitalize()
                formatted_name = ''.join(position)
            else:
                position = position.lower().capitalize()
                formatted_name += " " + position
                
        bid_entry["name"] = formatted_name
        bid_entry["bid"] = round(float(input("\nEnter bid: \n> ").replace("$", "")), 2)
        bid_entry["id"] = id
        bids.append(bid_entry)
        
        clear()
        more_bidders = int(input("\nIs there another bidder? \nEnter 1 for \"YES\" \nEnter 0 for \"NO\" \n> ").strip())
        if more_bidders == 1:
            clear()
    
    winning_bid = 0
    for bidder in bids:
        if bidder["bid"] > winning_bid:
            winners_name = bidder["name"]
            winners_bid = bidder["bid"]
            winning_bid = winners_bid
            
    print(f"\n{winners_name} won the aution with a bid of ${winners_bid:.2f}.\n")
    
if __name__ == "__main__":
    silent_auction()