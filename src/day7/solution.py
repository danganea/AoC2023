input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""
# Five of a kind, where all five cards have the same label: AAAAA
# Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
# One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
# High card, where all cards' labels are distinct: 23456

from collections import Counter

cards = reversed(["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"])

cards_to_index = {c: i for i, c in enumerate(cards)}


def card_to_index_list(card_str: str):
    return tuple(cards_to_index[c] for c in card_str)


def get_card_type(card_str: str):
    counter = Counter(card_str)

    if max(counter.values()) == 5:
        return 6
    elif max(counter.values()) == 4:
        return 5
    elif max(counter.values()) == 3 and min(counter.values()) == 2:
        return 4
    elif max(counter.values()) == 3:
        return 3
    elif sum(1 for v in counter.values() if v == 2) == 2:
        return 2
    elif max(counter.values()) == 2:
        return 1
    else:
        return 0


def _part1():
    cards = input.split()
    cards = [(cards[i], int(cards[i + 1])) for i in range(0, len(cards), 2)]

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
