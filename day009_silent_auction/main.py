import os
import time
import pandas
from art import auction_sign


def screen_clear():
    "Cleans terminal screen with 1 second delay."
    time.sleep(1)
    os.system("cls" if os.name == "nt" else "clear")


def parse_input(message):
    """Strip and lower case inputs."""
    return input(message).strip().lower()


def bid():
    """
    Prompt user for name and bid.
    """
    screen_clear()
    name = parse_input("What's your name?: ")
    bid = parse_input("What's your bid?: ")
    more_bids = parse_input("Any more bidders?: ")
    truthy = ["yes", "y", "1"]
    if more_bids.lower() in truthy:
        more_bids = True
    else:
        more_bids = False

    return {"name": name.lower(), "bid": int(bid), "more_bids": more_bids}


def auction():
    print(auction_sign)
    bidding = True
    bids = {}
    while bidding:
        bid_notes = bid()
        bids.update({bid_notes["name"]: bid_notes["bid"]})
        bidding = bid_notes["more_bids"]

    screen_clear()
    winners = [(n.capitalize(), b) for n, b in bids.items() if b == max(bids.values())]
    if len(winners) > 1:
        win_table = pandas.DataFrame(winners, columns=["Name", "Bid"])
        print("More than one winning:\n", win_table.to_string(index=False))
    else:
        print(f"CONGRATULATIONS: {winners[0][0]}\nBid:{winners[0][1]}")


if __name__ == "__main__":
    auction()
