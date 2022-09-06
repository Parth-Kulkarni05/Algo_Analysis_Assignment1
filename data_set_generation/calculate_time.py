import random
import os
from pathlib import Path

p = Path(__file__).with_name('log_out_file.txt')


with open(p) as f:
    
    f_list = [int(word.split()[2]) for word in f]

    print(round(sum(f_list) / len(f_list)))