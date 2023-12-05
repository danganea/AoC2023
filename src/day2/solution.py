# 12 red cubes, 13 green cubes, and 14 blue cubes
MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


def is_game_possible(game: str):
    all_rounds = game.strip().split(":")[1]
    rounds = all_rounds.split(";")

    maxes = {"red": 0, "green": 0, "blue": 0}

    for round in rounds:
        colors = round.strip().split(",")
        for color in colors:
            number, color = color.strip().split(" ")
            number = int(number)
            maxes[color] = max(maxes[color], number)

    if maxes["red"] > MAX_RED or maxes["blue"] > MAX_BLUE or maxes["green"] > MAX_GREEN:
        return False
    else:
        return True


def power_set_per_game(game: str):
    all_rounds = game.strip().split(":")[1]
    rounds = all_rounds.split(";")

    maxes = {"red": 0, "green": 0, "blue": 0}

    for round in rounds:
        colors = round.strip().split(",")
        for color in colors:
            number, color = color.strip().split(" ")
            number = int(number)
            maxes[color] = max(maxes[color], number)

    return maxes["red"] * maxes["blue"] * maxes["green"]


def _main_part_1(input):
    games = input.split("\n")
    sum_possible_games = sum(
        i for i in range(1, len(games) + 1) if is_game_possible(games[i - 1])
    )
    print(sum_possible_games)


def _main_part_2(input):
    games = input.split("\n")
    sum_power = sum(power_set_per_game(game) for game in games)

    print(sum_power)


if __name__ == "__main__":
    input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

    _main_part_1(input)
    _main_part_2(input)
