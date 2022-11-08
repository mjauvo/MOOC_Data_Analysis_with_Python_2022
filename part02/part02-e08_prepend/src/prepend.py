#!/usr/bin/env python3

"""
Create a class called Prepend. We create an instance of the class by giving a string as a parameter to the initializer. The initializer stores the parameter in an instance attribute start. The class also has a method write(s) which prints the string s prepended with the start string. An example of usage:

    p = Prepend("+++ ")
    p.write("Hello");

Will print

    +++ Hello
"""

class Prepend(object):

    # Add the methods of the class here

    def __init__(self, prepended_string):
        self.prepended_string = prepended_string

    def write(self, s):
        print(self.prepended_string + s)

    def main():
        pass

    if __name__ == "__main__":
        main()

p = Prepend("Well . . . ")
p.write("Hello")
