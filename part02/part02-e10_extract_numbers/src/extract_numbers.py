#!/usr/bin/env python3

# Gets a string s as a parameter and returns a list
# of number_list that can be both ints and floats.
def extract_numbers(s):
    number_list = []
    string_list = s.split()

    for word in string_list:
        # is an integer?
        try:
            number_list.append(int(word))
            print(f"- Integer: {word}")
        except (ValueError):
            # is a float?
            try:
                number_list.append(float(word))
                print(f"- Float: {word}")
            # is neither
            except (ValueError):
                print(f"- Element '{word}' is not a number!")

    return number_list

def main():
    s = "abd 123 1.2 test 13.2 -1"
    numbers = extract_numbers(s)
    print(numbers)

if __name__ == "__main__":
    main()
