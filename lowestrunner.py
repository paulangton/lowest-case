import sys
import lowest

def main(args):
    if len(args) > 1:
        print(lowest.lowest(args[1]))
    else:
        print("Usage: lowest <STR>")

if __name__ == '__main__':
    main(sys.argv)
