"""
    Pretty ugly solution this time, I'll need to refactor it at some point :)

    I included the bruteforce solution to part 2, which amounts to yielding all the seeds (so as to not consume memory) from a generator
    and then solving part 1 basically.
"""
import math
from dataclasses import dataclass, field
from typing import Iterable, Sequence

input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


@dataclass
class Range:
    destination_range_start: int
    source_range_start: int
    range_length: int

    # property for source_range_end
    @property
    def source_range_end(self):
        return self.source_range_start + self.range_length - 1

    def get_source_range_till(self):
        return self.source_range_start + self.range_length


@dataclass
class RangeMap:
    source_type: str
    destination_type: str
    ranges: list[Range] = field(default_factory=list)


def parse_ranges(range_substr: Sequence[str]) -> list[RangeMap]:
    ranges = []
    current_range = None
    for substr in range_substr:
        if not substr:
            assert current_range
            ranges.append(current_range)
            current_range = None
        elif "map" in substr:
            from_src, to_dst = substr.split(" map:")[0].split("-to-")
            current_range = RangeMap(from_src, to_dst)
        else:
            assert current_range
            dst_start, src_start, length = map(int, substr.split(" "))
            current_range.ranges.append(Range(dst_start, src_start, length))

    assert current_range
    ranges.append(current_range)
    return ranges


def _part1(seeds: list[int], rangeMaps: list[RangeMap]) -> None:
    current_seed_mapping = [s for s in seeds]

    for rangeMap in rangeMaps:  # Assumption is 'location' is last.
        for mapping_idx, curr_mapping in enumerate(current_seed_mapping):
            for range in rangeMap.ranges:
                if (range.source_range_start <= curr_mapping <= range.get_source_range_till()):
                    new_map_value = range.destination_range_start + (
                        curr_mapping - range.source_range_start
                    )
                    current_seed_mapping[mapping_idx] = new_map_value
                    break

    print(min(current_seed_mapping))


def intersect(r1_start, r1_end, r2_start, r2_end) -> tuple[int, int] | None:
    start = max(r1_start, r2_start)
    end = min(r1_end, r2_end)

    if start <= end:
        return (start, end)

    return None


def _part2(seeds: list[tuple[int, int]], mappings: list[RangeMap]) -> None:
    intervals = [s for s in seeds]
    next_ranges = []

    # sort ranges in mappings by source_range_start
    for mapping in mappings:
        mapping.ranges.sort(key=lambda r: r.source_range_start)


    for mapping in mappings:
        for interval in intervals:
            curr_start, curr_end = interval
            found_intersection = False
            for range in mapping.ranges:
                intersection = intersect(
                    curr_start,
                    curr_end,
                    range.source_range_start,
                    range.source_range_end,
                )

                if intersection is None:
                    continue

                intersection_start, intersection_end = intersection
                start_destination = range.destination_range_start + (
                    intersection_start - range.source_range_start
                )
                length_destination = intersection_end - intersection_start

                new_range = (start_destination, start_destination + length_destination)
                next_ranges.append(new_range)

                remaining_bit_left = (
                    (curr_start, intersection_start - 1)
                    if intersection_start > curr_start
                    else None
                )
                remaining_bit_right = (
                    (intersection_end + 1, curr_end)
                    if intersection_end < curr_end
                    else None
                )

                if remaining_bit_left is not None:
                    next_ranges.append(remaining_bit_left)

                if remaining_bit_right is not None:
                    intervals.append(remaining_bit_right)
                
                found_intersection = True

                break
            
            if not found_intersection:
                next_ranges.append(interval)

        intervals = next_ranges
        next_ranges = []


    starts = [s for s, _ in intervals]

    print(min(starts))


def _part2_bruteforce(seeds: Iterable[int], rangeMaps: list[RangeMap]) -> None:
    curr_mapping = None
    min_mapping = math.inf
    for seed in seeds:
        if curr_mapping is None:
            curr_mapping = seed

        for rangeMap in rangeMaps:  # Assumption is 'location' is last.
            for range in rangeMap.ranges:
                if (
                    range.source_range_start
                    <= curr_mapping
                    <= range.get_source_range_till()
                ):
                    new_map_value = range.destination_range_start + (
                        curr_mapping - range.source_range_start
                    )
                    curr_mapping = new_map_value
                    break

        min_mapping = min(min_mapping, curr_mapping)
        curr_mapping = None

    print(min_mapping)


def seed_yielder_bruteforce(seeds: list[int]) -> Iterable[int]:
    for i in range(0, len(seeds), 2):
        start = seeds[i]
        leng = seeds[i + 1]

        for j in range(start, start + leng):
            yield (j)


def _main():
    seeds = [
        int(num.strip())
        for num in input.split("\n")[0].split(":")[1].split(" ")
        if len(num.strip()) != 0
    ]

    range_substring = input.split("\n")[2:]

    ranges: list[RangeMap] = parse_ranges(range_substring)

    # _part1(seeds, ranges)
    # _part2_bruteforce(seed_yielder_bruteforce(seeds), ranges)
    seeds = [(seeds[i], seeds[i] + seeds[i + 1] - 1) for i in range(0, len(seeds), 2)]
    _part2(seeds, ranges)


if __name__ == "__main__":
    with open("src/day5/input.in") as f:
        input = f.read()
    _main()
