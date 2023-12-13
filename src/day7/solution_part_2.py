input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

# Input with all card types
# Five of a kind, where all five cards have the same label: AAAAA
# Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
# One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
# High card, where all cards' labels are distinct: 23456

from collections import Counter

cards = reversed(["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"])

cards_to_index = {c: i for i, c in enumerate(cards)}


def card_to_index_list(card_str: str):
    return tuple(cards_to_index[c] for c in card_str)


def best_is_full_house(counter) -> bool:
    basic_condition = max(counter.values()) == 3 and min(counter.values()) == 2
    if basic_condition:
        return True

    jokers = counter["J"]
    values = [v for k, v in counter.items() if k != "J"]
    # Could have just checked num of keys remaining after J. If 2 we good?
    if jokers in [1, 2] and len(values) == 2:
        return True

    return False


def best_is_two_kind(counter) -> bool:
    basic_condition = sum(1 for v in counter.values() if v == 2) == 2
    jokers = counter["J"]

    if basic_condition:
        return True

    if jokers == 1 and max(counter.values()) == 2:
        return True

    if jokers == 2:
        return True

    return False

    # Got 3 of a kind and 2 Js -> Already handled

    # Got 2 of A and 2 of B and 1 J
    # Got 2 of A and 1 of B and 2 Js

    # Got 1 of A, 1 of B and 3 Js -> already handled cause we'd rather make 4 of a kind


def get_card_type(card_str: str):
    counter = Counter(card_str)
    jokers = counter["J"]

    max_val = max(counter.values())
    max_without_jokers = max([v for k, v in counter.items() if k != "J"], default=0)

    if max(counter.values()) == 5 or max_without_jokers + jokers >= 5:
        return 6
    elif max(counter.values()) == 4 or max_without_jokers + jokers >= 4:
        return 5
    elif best_is_full_house(counter):
        return 4
    elif max(counter.values()) == 3 or max_val + jokers >= 3:
        return 3
    elif best_is_two_kind(counter):  # two kind
        return 2
    elif max(counter.values()) == 2 or max_val + jokers == 2:  # pair
        return 1
    else:
        return 0


def _part1():
    cards = input.split()
    cards = [(cards[i], int(cards[i + 1])) for i in range(0, len(cards), 2)]

    # cards_to_order = [(get_card_type(card), card_to_index_list(card), bid, card) for card, bid in cards]
    cards_to_order = [
        (get_card_type(card), card_to_index_list(card), bid) for card, bid in cards
    ]

    cards_to_order.sort()

    print(sum(bid * (i + 1) for i, (_, _, bid) in enumerate(cards_to_order)))


if __name__ == "__main__":
    with open("src/day7/input.in") as f:
        input = f.read()
    _part1()

    pass
