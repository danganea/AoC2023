digit_map = {str(i): i for i in range(10)}

digit_map.update(
    {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "zero": 0,
    }
)


def get_calibration_value(line: str) -> int:
    first_digit = None
    first_found = len(line)
    for digit in digit_map:
        index = line.find(digit)
        if index != -1 and index < first_found:
            first_found = index
            first_digit = digit_map[digit]

    last_found = -1
    last_digit = None
    for digit in digit_map:
        index = line.rfind(digit)
        if index != -1 and index > last_found:
            last_found = index
            last_digit = digit_map[digit]

    assert last_digit
    assert first_digit

    return first_digit * 10 + last_digit


def _main(input):
    result = sum(get_calibration_value(line) for line in input.split())
    result_simple = sum(get_calibration_value(line) for line in input.split())
    print(result)
    print(result_simple)


if __name__ == "__main__":
    with open("src/day1/input.in") as f:
        raw_input = f.read()

    assert get_calibration_value("1twone") == 11
    assert get_calibration_value("1abc2") == 12
    assert get_calibration_value("onetwo") == 12
    assert get_calibration_value("pqr3stu8vwx") == 38
    assert get_calibration_value("aqone2threexyz") == 13
    assert get_calibration_value("onetwoonetwoone") == 11

    _main(raw_input)
