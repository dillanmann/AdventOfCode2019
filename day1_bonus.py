# run with `cat <input_file.txt> | py day1_bonus.py`
import math
import sys

def calculate_fuel(module_mass):
    module_total = 0

    mass = module_mass
    while True:
        fuel = math.floor(mass / 3) - 2
        if fuel <= 0:
            break

        module_total += fuel
        mass = fuel

    return module_total

if __name__ == "__main__":
    inputs = [int(mass) for mass in sys.stdin]
    totals = []
    for mass in inputs:
        totals.append(calculate_fuel(mass))  

    print("Total mass = {}".format(sum(totals)))