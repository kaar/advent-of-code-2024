import sys


# https://adventofcode.com/2024/day/1#part2
def main():
    # Read from stdin
    l_values = []
    r_values = []
    for line in sys.stdin:
        # Split the lines into separate lists
        values = line.strip().split()
        l_values.append(int(values[0]))
        r_values.append(int(values[1]))
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


if __name__ == "__main__":
    main()
