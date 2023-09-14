def count_increasing_measurements(input_string):
    # Since input is multi-line string, we need to split the string by lines and convert each line to an integer
    measurements = convert_string_to_int_list(input_string)
    count = 0

    # Iterate through measurements starting from the second one
    for i in range(1, len(measurements)):
        if measurements[i] > measurements[i - 1]:
            count += 1
    return count


def count_increasing_sums(input_string):
    measurements = convert_string_to_int_list(input_string)

    if len(measurements) < 3:
        return 0

    count = 0
    previous_sum = sum(
        measurements[:3]
    )  # Calculate the sum of the first three measurements

    # Since we know the sum of first 3 counts, we start iterating from 4th
    for i in range(3, len(measurements)):
        current_sum = sum(measurements[i - 2 : i + 1])

        if current_sum > previous_sum:
            count += 1

        previous_sum = current_sum
    return count


def convert_string_to_int_list(string):
    return [int(line.strip()) for line in string.strip().split("\n")]


if __name__ == "__main__":
    sonar_input = open("day1_input.txt", "r").read()

    increasing_count = count_increasing_measurements(sonar_input)
    increasing_sums = count_increasing_sums(sonar_input)

    print(f"The increasing count is: {increasing_count}")
    print(f"The increasing count of sums is: {increasing_sums}")
