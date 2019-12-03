#run with `cat day2.in.txt | py day2.py`
import sys

values = []

def load_values():
    global values
    values = [int(value) for value in sys.stdin.readline().split(',')]


def iterate_values():
    global values
    index = 0
    while True:
        op_code = values[index]
        if op_code == 1:
            add(values[index + 1], values[index + 2], values[index + 3])
        elif op_code == 2:
            multiply(values[index + 1], values[index + 2], values[index + 3])
        elif op_code == 99:
            break
        else:
            raise Exception("Invalid op code {}".format(op_code))

        # Go to next op
        index = index + 4


def add(first, second, output_index):
    global values
    values[output_index] = values[first] + values[second]

def multiply(first, second, output_index):
    global values
    values[output_index] = values[first] * values[second]

def set_1202():
    global values
    values[1] = 12
    values[2] = 2

if __name__ == "__main__":
    load_values()
    set_1202()
    iterate_values()
    print(values[0])