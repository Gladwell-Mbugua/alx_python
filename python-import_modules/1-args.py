#!/usr/bin/env/python3

import sys 


def main():
    args = sys.argv[1:]
    num_args = len(args)

    print(f"Number of argument(s): {num_args}", end="")
    if num_args == 1:
        print("{} argument:".format(num_args), end="")
    elif num_args > 1:
        print("{} arguments:".format(num_args), end="")
    else:
        print(".", end="")

        print()
        return

    print(":")

    for i, arg in enumerate(args, start=1):
        print(f"{i}: {arg}")

if __name__ == "__main__":
    main()
    
