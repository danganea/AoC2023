import math
input = """Time:      7  15   30
Distance:  9  40  200"""

def parse(s: str):
    """
        Parse time and distance into list[tuple[int,int]]
    """

    lines = s.split("\n")
    times = lines[0].split()[1:]
    distances = lines[1].split()[1:]

    return list(zip(map(int, times), map(int, distances)))


def parse_part2(s: str) -> list[tuple[int,int]]:
    """
        Now you need to merge all the numbers as one. so there's only one time and one distance
    """

    lines = s.split("\n")
    time = lines[0].split()[1:]
    distance = lines[1].split()[1:]

    time_int = int("".join(time))
    distance_int = int("".join(distance))

    return [(time_int, distance_int)]





# One can also solve this inequality but this is fast enough for both parts
# clicktime * (time - click_time) > distance
def solve(races: list[tuple[int,int]]) -> None:
    prod = 1
    for i, race in enumerate(races):
        count_beat = 0
        time, distance = race

        for click_time in range(time + 1):
            speed = click_time
            remaining_time = time - click_time

            if speed * remaining_time > distance:
                # print(i, click_time)
                count_beat += 1

        prod *= count_beat

    
    # print product of all
    # print(vals)
    print(prod)


def _main():
    # races = parse(input)
    # _part1(races)
    races = parse_part2(input)
    solve(races)
    print(races)
    # _part2(input)




if __name__ == "__main__":
    with open("src/day6/input.in") as f:
        input = f.read()
    _main()