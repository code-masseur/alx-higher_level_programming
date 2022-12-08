#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    
    if len(sys.argv) != 4:
        print('Usage: {:s} <a> <operator> <b>'.format(sys.argv[0]))
        sys.exit(1)
    if sys.argv[2] not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]

    if operator == '+':
        print('{} + {} = {}'.format(a, operator, b, add(a, b)))
    elif operator == '-':
        print('{} - {} = {}'.format(a, operator, b, sub(a, b)))
    elif operator == '*':
        print('{} * {} = {}'.format(a, operator, b, mul(a, b)))
    else:
        print('{} / {} = {}'.format(a, operator, b, div(a, b)))
