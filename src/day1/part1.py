from typing import Iterable


def get_first_digit(line: Iterable) -> int:
    for c in line:
        if str.isdigit(c):
            return int(c)

    assert False


def get_calibration_value(line: str) -> int:
    first_digit = get_first_digit(line)
    last_digit = get_first_digit(reversed(line))
    return first_digit * 10 + last_digit


def _main(input):
    result = sum(get_calibration_value(line) for line in input.split())
    print(result)


if __name__ == "__main__":
    assert get_calibration_value("1abc2") == 12
    assert get_calibration_value("pqr3stu8vwx") == 38
    assert get_calibration_value("a1b2c3d4e5f") == 15
    assert get_calibration_value("treb7uchet") == 77

    raw_input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

    _main(raw_input)
