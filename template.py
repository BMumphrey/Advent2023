import sys

def main():
    infile = sys.argv[1]
    with open(infile, 'r') as f:
        input = [x.strip() for x in f.readlines()]

if __name__ == "__main__":
    main()