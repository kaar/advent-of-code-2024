#!/usr/bin/env -S uv run
import re
import sys


def mem_check(input):
    # Regex to find mul(X,Y) where X and Y are integers \d+
    pattern = re.compile(r"mul\((\d+),(\d+)\)")
    matches = pattern.findall(input)
    return sum(int(x) * int(y) for x, y in matches)


def test_part_1():
    input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    expected = 161
    assert mem_check(input) == expected

def run_part_1():
    tot_sum = 0
    for line in sys.stdin:
        tot_sum += mem_check(line.strip())

    print(tot_sum)

if __name__ == "__main__":
    # test_part_1()
    run_part_1()
