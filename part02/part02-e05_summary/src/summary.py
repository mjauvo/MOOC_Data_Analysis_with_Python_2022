#!/usr/bin/env python3

import sys
import math

# Gets a filename as a parameter, input file containing
# a floating point number on each line of the file. Reads
# these numbers and then return a triple containing the sum,
# average, and standard deviation of these numbers for the
# file. Lines that do not represent numbers are ignored.
def summary(filename):
    file_numbers = []

    with open(filename) as file:
        for number in file:
            try:
                file_numbers.append(float(number))
            except ValueError:
                print(f"\tConversion of an element to type 'float' failed!! Element: {number}")

        # Sum        
        summary_sum = sum(file_numbers)

        # Average
        summary_average = sum(file_numbers) / len(file_numbers)

        # Standard deviation
        numerator = 0

        for x in file_numbers:
            numerator += (x - summary_average) ** 2
        denominator = len(file_numbers)-1

        summary_std_dev = math.sqrt(numerator / denominator)

    return (summary_sum, summary_average, summary_std_dev)

def main():
    for file in sys.argv[1:]:
        summary_sum, summary_average, summary_std_dev = summary(file)
        print(f"File: {file} Sum: {summary_sum:.6f} Average: {summary_average:.6f} Stddev: {summary_std_dev:.6f}")

if __name__ == "__main__":
    main()
