# run with `cat <input_file.txt> | py day1.py`
import math
import sys

def calculate_fuel(module_mass):
    return math.floor(int(module_mass) / 3) - 2

if __name__ == "__main__":
    total = 0
    for mass in sys.stdin:
        total += calculate_fuel(mass)

    print("Total mass = {}".format(total))