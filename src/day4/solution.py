from dataclasses import dataclass

input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


@dataclass
class Card:
    index: int
    winning: list[int]
    ours: list[int]


def parse_to_card(line: str) -> Card:
    card_part, numbers = line.strip().split(":")
    card_index = int(card_part.split(" ")[-1])

    def parse_numbers(numbers_str: str) -> list[int]:
        return [int(n) for n in numbers_str.strip().split(" ") if len(n) != 0]

    winning_str, ours_str = numbers.strip().split("|")

    winning, mine = parse_numbers(winning_str), parse_numbers(ours_str)

    return Card(card_index, winning, mine)


def get_matches(card: Card) -> int:
    winning = set(card.winning)
    mine = set(card.ours)

    return len(winning & mine)


def get_score_part1(matches: int) -> int:
    if matches == 0:
        return 0

    return 1 << (matches - 1)


def part_1(cards: list[Card]) -> None:
    result = sum((get_score_part1(get_matches(card))) for card in cards)
    print(result)


def part_2(cards: list[Card]) -> None:
    num_copies = [1 for _ in cards]
    for i, card in enumerate(cards):
        matches = get_matches(card)
        for j in range(matches):
            num_copies[i + j + 1] = num_copies[i + j + 1] + num_copies[i]

    print(sum(num_copies))


def _main():
    cards = [parse_to_card(line) for line in input.split("\n")]
    part_1(cards)
    part_2(cards)

if __name__ == "__main__":
    # with open("src/day4/input.in") as f:
    #     input = f.read()

    _main()
