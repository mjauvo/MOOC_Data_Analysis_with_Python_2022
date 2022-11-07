#!/usr/bin/env python3

# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle

def main():
    side1 = 3.0
    side2 = 4.0

    print(f"- Side 1: {side1}")
    print(f"- Side 2: {side2}")
    print(f"- Hypothenuse: {triangle.hypothenuse(side1, side2)}")
    print(f"- Area: {triangle.area(side1, side2)}")

if __name__ == "__main__":
    main()
