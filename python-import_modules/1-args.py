#!/usr/bin/env/python3

import sys 


def main():
    args = sys.argv[1:]
    num_args = len(args)

    print(f"Number of argument(s): {num_args}", end="")
    if num_args == 1:
        print(" followed by argument:", end="")
    elif num_args > 1:
        print(" followed by arguments:", end="")
    else:
        print(".", end="")

    print()

    for i, arg in enumerate(args, start=1):
        print(f"{i}: {arg}")

if __name__ == "__main__":
    main()


    