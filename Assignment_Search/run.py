import argparse
import os
parser = argparse.ArgumentParser("Parser for run")
parser.add_argument("--heuristic",type=str,default="misplaced",choices=["manhattan","misplaced"])
args = parser.parse_args()
for i in range(0,100):
    os.system(f"python main.py --start inputs/{i}.txt --goal goals/{i}.txt --heuristic {args.heuristic}")