#!/usr/bin/env -S uv run
import sys


def is_safe(levels: list[int]):
    going_up = 1 if levels[0] > levels[1] else -1
    for x, y in zip(levels, levels[1:]):
        distance = (x - y) * going_up
        if 1 <= distance <= 3:
            continue
        return False
    return True


def is_safe_with_damp(levels):
    for i in range(len(levels)):
        if is_safe(levels[:i] + levels[i + 1 :]):
            return True

    return False


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


def part_1_alt_2(report):
    print(sum(is_safe(levels) for levels in report))


def part_2(reports):
    print(sum(is_safe_with_damp(levels) for levels in reports))


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
