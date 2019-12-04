# run with `cat <input_file> | py day4_bonus.py`
import sys

def never_decreases(digits):
    last = digits[0]
    for digit in digits:
        if digit < last:
            return False
        last = digit

    return True
        
def valid_doubles(digits):
    has_double = False
    for i in range(1, len(digits)):
        if digits[i] == digits[i-1]:
            if digits.count(digits[i]) > 2:
                continue
            else:
                has_double = True

    return has_double

if __name__ == "__main__":
    matches = []

    input = "271973-785961"
    print(input)
    lower_bound, upper_bound = tuple([int(s) for s in input.split('-')])
    for num in range(lower_bound, upper_bound + 1):
        digits = [int(d) for d in str(num)]
        if never_decreases(digits) and valid_doubles(digits):
            matches.append(num)

    print(len(matches))