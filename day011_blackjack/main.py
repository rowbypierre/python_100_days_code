import random
from art import logo, win_ascii, lose_ascii, draw_ascii

deck = [card for card in range(2, 12) for _ in (range(3) if card == 10 else range(1))]

DEALER_HIT_LIMIT = 17
BLACKJACK = 21


def deal_card():
    """Return random card (int) from deck."""
    return random.choice(seq=deck)


def deal_hand():
    """Return hand (list) of two cards (int)."""
    return [deal_card() for _ in range(2)]


def dealer_needs_card(hand):
    """Confirms (bool) if dealer is to be dealt."""
    global DEALER_HIT_LIMIT
    return sum(hand) < DEALER_HIT_LIMIT


def blackjack(hand):
    """Confirms (bool) if hand (list) has blackjack."""
    return sum(hand) == BLACKJACK


def bust(hand):
    """Confirms (bool) if hand (list) > blackjack."""
    return sum(hand) > BLACKJACK


def print_hands(dealer_hand, your_hand):
    """Dealer and player hand terminal print screen."""
    print(f"\nDealer:\t\t{dealer_hand}")
    print(f"Your hand:\t{your_hand}")


def ace_convert(hand):
    """Return hand (list) with ace cards (11) as as value 1 (int)."""
    if bust(hand):
        return [1 if card == 11 else card for card in hand]
    else:
        return hand


def draw(hand1, hand2):
    """Confirm (bool) twos hands (list) have same summation."""
    return sum(hand1) == sum(hand2)


dealer_hand = deal_hand()
your_hand = deal_hand()
playing = True
while playing:
    print(logo)
    dealer_maskhand = [x for x in dealer_hand[: len(dealer_hand) - 1]] + ["X"]
    print_hands(dealer_maskhand, your_hand)

    get_input = True
    while get_input:
        try:
            deal = input("h (Hit) | s (Stand): ").strip().lower()
            if deal not in ["h", "s"]:
                raise ValueError(f"'{deal}' is not 'h' or 's'.")
            else:
                get_input = not get_input
        except Exception as error:
            print(f"Error: {error}")

    if deal.isalpha() and deal in ["h", "s"]:
        if deal == "h":
            your_hand.append(deal_card())
        if dealer_needs_card(dealer_hand):
            dealer_hand.append(deal_card())

        dealer_hand = ace_convert(dealer_hand)
        your_hand = ace_convert(your_hand)

        if (
            blackjack(dealer_hand)
            or bust(your_hand)
            or (sum(your_hand) < sum(dealer_hand) and not bust(dealer_hand))
        ):
            print(lose_ascii)
            print_hands(dealer_hand, your_hand)
            playing = False
        elif draw(dealer_hand, your_hand):
            print(draw_ascii)
            print_hands(dealer_hand, your_hand)
            playing = False
        else:
            print(win_ascii)
            print_hands(dealer_hand, your_hand)
            playing = False
