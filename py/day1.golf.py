# run with `cat <input_file.txt> | py day1.golf.py`
import math
import sys

print(sum(map(lambda f: math.floor(f/3)-2, [int(m) for m in sys.stdin])))