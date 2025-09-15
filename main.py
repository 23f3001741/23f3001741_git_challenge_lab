import argparse
from operations import add , subtract , multiply
def main():
    parser = argparse.ArgumentParser(description="Arithmetic operations CLI")
    parser.add_argument("op", choices=ops.keys(), help="operation: add, sub, mul")
    parser.add_argument("a",type=float,help="first operand")
    parser.add_argument("b",type=float,help="second operand")
    args = parser.parse_args()

    fn = ops[args.op]
    try:
        result = fn(args.a, args.b)
    except Exception as e:
        print("error:", e)
    else:
        print("Result:",result)

if __name__ == "__main__":
    main()