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


def part_1_alt(reports):
    safe_count = 0
    for levels in reports:
        distances = [x - y for x, y in zip(levels, levels[1:])]
        if all(abs(x) in [1, 2, 3] for x in distances):
            if all(x > 0 for x in distances):
                safe_count += 1
            if all(x < 0 for x in distances):
                safe_count += 1
    print(safe_count)


def part_2(reports):
    safe_count = 0
    for levels in reports:
        distances = [x - y for x, y in zip(levels, levels[1:])]
        safe_distances = len([x for x in distances if abs(x) in [1, 2, 3]])
        if safe_distances >= len(distances) - 1:
            increase_count = len([x for x in distances if x > 0])
            if increase_count >= len(distances) - 1:
                safe_count += 1
            decrease_count = len([x for x in distances if x < 0])
            if decrease_count >= len(distances) - 1:
                safe_count += 1
    print(safe_count)


def main():
    # Read from stdin
    # https://adventofcode.com/2024/day/2/input
    reports = []
    for line in sys.stdin:
        levels = [int(x) for x in line.strip().split()]
        reports.append(levels)

    part_2(reports)


if __name__ == "__main__":
    main()
