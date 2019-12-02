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

def set_noun_and_verb(noun, verb):
    global values
    values[1] = noun
    values[2] = verb

if __name__ == "__main__":
    target = 19690720
    for noun in range(0, 100):
        for verb in range(0, 100):
            load_values()
            set_noun_and_verb(noun, verb)
            iterate_values()
            if values[0] == target:
                print("Noun={}\nVerb={}".format(noun, verb))
                break

    print(values[0])