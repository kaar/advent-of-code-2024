#!/usr/bin/env -S uv run
import sys


def part_1(reports):
    safe_count = 0
    for levels in reports:
        distances = [x - y for x, y in zip(levels, levels[1:])]
        if not all(abs(x) in [1, 2, 3] for x in distances):
            continue
        if all(x > 0 for x in distances):
            safe_count += 1
        if all(x < 0 for x in distances):
            safe_count += 1
    print(safe_count)


def main():
    # Read from stdin
    # https://adventofcode.com/2024/day/2/input
    # https://adventofcode.com/2024/day/1/input
    reports = []
    for line in sys.stdin:
        levels = [int(x) for x in line.strip().split()]
        reports.append(levels)

    part_1(reports)


if __name__ == "__main__":
    main()
