import sys
import re

digits = {
    "one": 1, "1": 1,
    "two": 2, "2": 2,
    "three": 3, "3": 3,
    "four": 4, "4": 4,
    "five": 5, "5": 5,
    "six": 6, "6": 6,
    "seven": 7, "7": 7,
    "eight": 8, "8": 8,
    "nine": 9, "9": 9,
    "zero": 0, "0": 0,
}

def calibration_digits(s):
    s_ints = re.sub("[^0-9]", "", s)
    return int(f"{s_ints[0]}{s_ints[-1]}")

def calibration_digits_p2(s):
    d1 = ""
    d2 = ""
    for i in range(len(s)):
        for digit in digits.keys():
            if s[i:].startswith(digit) and d1 == "":
                d1 = digits[digit]
            if s[len(s) - i - 1:].startswith(digit) and d2 == "":
                d2 = digits[digit]
    print(d1, d2)
    return int(f"{d1}{d2}")
    
def main():
    infile = sys.argv[1]
    with open(infile, 'r') as f:
        input = [x.strip() for x in f.readlines()]
    
    print(f"Part 1: {sum([calibration_digits(x) for x in input])}")

    print(f"Part 2: {sum([calibration_digits_p2(x) for x in input])}")

if __name__ == "__main__":
    main()