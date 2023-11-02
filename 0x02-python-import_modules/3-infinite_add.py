#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    total = 0

    for arg in args:
        try:
            num = int(arg)
            total += num
        except ValueError:
            print(f"Error: '{arg}' is not a valid integer.")

    print(total)
