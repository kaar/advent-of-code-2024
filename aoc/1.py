#!/usr/bin/env -S uv run
import sys


def part_1(l_values, r_values):
    # https://adventofcode.com/2024/day/1#part1
    # Sort the lists
    l_values.sort()
    r_values.sort()
    sum_distance = 0
    # Zip the lists and iterate over them
    for l_value, r_value in zip(l_values, r_values):
        # Take the distance between the two values
        distance = abs(l_value - r_value)
        sum_distance += distance
    print(sum_distance)


def part_2(l_values, r_values):
    # https://adventofcode.com/2024/day/1#part2
    r_values_counts = {}
    similarity_score = 0
    for value in l_values:
        # Count the number of times the value appears in the r_values
        if value not in r_values_counts:
            r_values_counts[value] = r_values.count(value)
        similarity_score += value * r_values_counts[value]
    print(similarity_score)


def main():
    # Read from stdin
    # https://adventofcode.com/2024/day/1/input
    l_values = []
    r_values = []
    for line in sys.stdin:
        # Split the lines into separate lists
        values = line.strip().split()
        l_values.append(int(values[0]))
        r_values.append(int(values[1]))

    part_2(l_values, r_values)


if __name__ == "__main__":
    main()
