# run with `cat <input_file.txt> | py day1.golf.py`
import sys

print(sum(int(m)//3-2 for m in sys.stdin))