#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    outcome = 0
    for args in sys.argv:
        if args != sys.argv[0]:
            outcome += int(args)
    print(outcome)
