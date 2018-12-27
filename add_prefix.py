import os
import argparse

parser = argparse.ArgumentParser('add prefix tool')
parser.add_argument('dir')
parser.add_argument('prefix')
args = parser.parse_args()

for root, folders, fnames in os.walk(args.dir):
    for fname in fnames:
        src = os.path.join(root, fname)
        target = os.path.join(root, args.prefix+fname)
        os.rename(src, target)
        print(f"{src} => {target}")