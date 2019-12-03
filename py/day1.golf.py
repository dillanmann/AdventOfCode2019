# run with `cat <input_file.txt> | py day1.golf.py`
import sys

print(sum(map(lambda f: int(f/3-2), [int(m) for m in sys.stdin])))